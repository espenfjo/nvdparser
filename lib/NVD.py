import logging
import http.client
import sys
import time
from threading import Timer
from threading import active_count
from threading import Lock
import os
import urllib.request

import lib.nvd._nvd as _nvd

from lib.mongodb import MongoDB
from lib.NVDXMPP import NVDXMPP


class NVD(object):
    CHECK_INTERVAL = 1800

    def __init__(self, config):
        self.config = config
        self.logger = logging.getLogger("NVD")
        self.database = MongoDB(self)
        self.xmpp = NVDXMPP(self)

        if self.config.importxml:
            self.import_xml()
        else:
            self.update()
            self.xmpp.run()


    def import_xml(self):
        """
        Import XML from file to Database.
        Will import new entries, or update old entries.
        """
        self.parse_nvd(self.config.importxml)


    def parse_nvd(self, xmlfile=None):
        """ Parse the XML and insert the CVE IDs into the database """


        if xmlfile and os.path.isfile(xmlfile):
            self.logger.info("Importing {} into database".format(xmlfile))
            with open(xmlfile, 'r') as f:
                xml = f.read()
        else:
            self.logger.debug("Fetching XML from mongodb")
            mongo_xml = self.database.collection.find_one({"xml": {'$exists': True}})
            if not mongo_xml:
                self.logger.error("Could not find XML in MongoDB")
                return 0
            xml = mongo_xml['xml']['data']

        self.logger.info("Parsing XML data")
        nvd_data = _nvd.CreateFromDocument(xml)
        for entry in nvd_data.entry:
            vulnerability = {}
            if "REJECT" in entry.summary:
                continue
            vulnerability['product'] = []
            if entry.vulnerable_software_list:
                product_list = entry.vulnerable_software_list.product
                for product in product_list:
                    try:
                        vulnerability['product'].append({
                            "vendor": product.split(':')[2],
                            "product": product.split(':')[3],
                            "version": product.split(':')[4]
                        })
                    except IndexError as e:
                        self.logger.error(e)
            vulnerability['cve_id'] = entry.cve_id
            vulnerability['publish_date'] = str(entry.published_datetime)
            vulnerability['update_date'] = str(entry.last_modified_datetime)
            vulnerability['summary'] = entry.summary
            vulnerability['cvss'] = None
            vulnerability['vector'] = None

            if entry.cvss:
                vulnerability['cvss'] = str(entry.cvss.base_metrics[0].score)
                vulnerability['vector'] = entry.cvss.base_metrics[0].access_vector.value()

            write_result = self.database.collection.update(
                {"cve_id": entry.cve_id},
                {"$set": {"vulnerability": vulnerability}},
                upsert=True
            )
            self.logger.debug( write_result )
            if write_result['nModified'] > 0:
                if not self.config.importxml:
                    self.xmpp.updated(vulnerability)
                self.logger.info("{} has been updated".format(entry.cve_id))
            elif write_result['updatedExisting'] == False:
                if not self.config.importxml:
                    self.xmpp.new(vulnerability)
                self.logger.debug("Inserting {} into DB".format(entry.cve_id))


    def download_if_needed(self):
        """ Downloads a new and updated NVD recent XML if needed """

        url = 'http://static.nvd.nist.gov/feeds/xml/cve/nvdcve-2.0-Recent.xml'
#        url = "https://blog.mrfjo.org/nvdcve-2.0-Recent.xml"
        request = urllib.request.Request(url)
        request.get_method = lambda: 'HEAD'
        try:
            self.logger.debug("HEADing {}".format(url))
            response = urllib.request.urlopen(request)
        except urllib.error.HTTPError as e:
            self.logger.error('HTTPError = ' + str(e.code))
            sys.exit(1)
        except urllib.error.URLError as e:
            self.logger.error('URLError = ' + str(e.reason))
            sys.exit(1)
        except http.client.HTTPException as e:
            self.logger.error('HTTPException')
            sys.exit(1)
        except Exception:
            import traceback
            self.logger.error('generic exception: ' + traceback.format_exc())
            sys.exit(1)

        modified = dict(response.info())['Last-Modified']
        modified_time = time.mktime(time.strptime(modified, '%a, %d %b %Y %H:%M:%S %Z'))
        self.logger.info("Last-Modified of the remote XML: {}".format(modified))

        self.logger.debug("Fetching XML from mongodb")
        mongo_xml = self.database.collection.find_one({"xml": {'$exists': True}})
        if mongo_xml:
            self.logger.info("Local XML age: {}".format(time.ctime(mongo_xml['xml']['mtime'])))
            if mongo_xml['xml']['mtime'] >= modified_time:
                if self.config.force:
                    self.logger.info("Local XML is unchanged from remote. But forcing download")
                else:
                    self.logger.info("Local XML is unchanged from remote. Skipping download")
                    return 0

        request.get_method = lambda: 'GET'
        try:
            self.logger.debug("GETing {}".format(url))
            response = urllib.request.urlopen(request)
        except urllib2.error.HTTPError as e:
            self.logger.error('HTTPError = ' + str(e.code))
            sys.exit(1)
        except urllib2.error.URLError as e:
            self.logger.error('URLError = ' + str(e.reason))
            sys.exit(1)
        except http.client.HTTPException as e:
            self.logger.error('HTTPException')
            sys.exit(1)
        except Exception:
            import traceback
            self.logger.error('generic exception: ' + traceback.format_exc())
            sys.exit(1)

        xml = {
            "xml": {
                "mtime": modified_time,
                "data": response.read()
            }
        }
        self.database.collection.update({"xml": {'$exists': True}}, xml, upsert=True)
        return 1

    def update(self):
        """ Update timer. Downloads the NVD XML every CHECK_INTERVAL """

        self.logger.info("Hitting update interval ({}), downloading new XML".format(self.CHECK_INTERVAL))
        self.logger.debug("Active threads: {}".format(active_count()))
        Timer(self.CHECK_INTERVAL, self.update).start()

        with Lock():
            if self.download_if_needed():
                self.parse_nvd()
                return 1
        return 0


    def find_cve(self, cve):
        """ Search for and return CVE entry """
        return self.database.collection.find_one({"cve_id": cve})
