import copy
import logging
import http.client
import time
from threading import Timer
from threading import active_count
from threading import Lock
import os
import sys
import urllib.request
import zlib

import lib.nvd._nvd as _nvd

from lib.mongodb import MongoDB
from lib.NVDXMPP import NVDXMPP
from lib.Vulnerability import Vulnerability
from lib.Product import Product


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
            if not self.config.disablexmpp:
                self.xmpp.run()
            self.update()

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
            vulnerability = Vulnerability()
            if "REJECT" in entry.summary:
                continue
            if entry.vulnerable_software_list:
                vulnerability.cpe = list(entry.vulnerable_software_list.product)
                for cpe in entry.vulnerable_software_list.product:
                    product = Product(cpe)
                    vulnerability.product.append(product)

            vulnerability.cve_id = entry.cve_id
            vulnerability.publish_date = str(entry.published_datetime)
            vulnerability.update_date = str(entry.last_modified_datetime)
            vulnerability.summary = entry.summary
            vulnerability.cvss = None
            vulnerability.vector = None

            if entry.cvss:
                vulnerability.cvss = str(entry.cvss.base_metrics[0].score)
                vulnerability.vector = entry.cvss.base_metrics[0].access_vector.value()

            try:
                vulnerability_raw = copy.deepcopy(vulnerability)  # The Transform in Product chagnes the vulnerability object
            except copy.error as e:
                self.logger.error(e)

            existing = Vulnerability(self.find_cve(entry.cve_id))
            if existing:
                self.logger.info("We have {} from before with CVSS={}, new is={}".format(existing.cve_id, existing.cvss, vulnerability.cvss))
            write_result = self.database.collection.update(
                {"cve_id": entry.cve_id},
                {"$set": {"vulnerability": vulnerability.__dict__}},
                upsert=True, manipulate=True
            )
            self.logger.debug(write_result)

            if write_result['nModified'] > 0:
                if not self.config.importxml:
                    if existing.cvss == vulnerability.cvss:
                        self.logger.debug("Existing CVSS of {} equals this CVSS of {}, skipping print".format(existing.cvss, vulnerability.cvss))
                    else:
                        self.xmpp.updated(vulnerability_raw, vulnerability.publish_date)
                self.logger.info("{} has been updated".format(entry.cve_id))
            elif existing is False or write_result['updatedExisting'] is False:
                if not self.config.importxml:
                    self.xmpp.new(vulnerability_raw)
                self.logger.debug("Inserting {} into DB".format(entry.cve_id))

    def download_if_needed(self, force=False):
        """ Downloads a new and updated NVD recent XML if needed """

        url = 'http://static.nvd.nist.gov/feeds/xml/cve/nvdcve-2.0-Recent.xml.gz'
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
                if self.config.force or force:
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

        gzip = zlib.decompressobj(16 + zlib.MAX_WBITS)
        xml = {
            "xml": {
                "mtime": modified_time,
                "data": gzip.decompress(response.read())
            }
        }
        self.database.collection.update({"xml": {'$exists': True}}, xml, upsert=True)
        return 1

    def update(self, force=False):
        """ Update timer. Downloads the NVD XML every CHECK_INTERVAL """

        self.logger.info("Hitting update interval ({}), downloading new XML".format(self.CHECK_INTERVAL))
        self.logger.debug("Active threads: {}".format(active_count()))
        Timer(self.CHECK_INTERVAL, self.update).start()

        with Lock():
            if self.download_if_needed(force=force):
                self.parse_nvd()
                return 1
        return 0

    def find_cve(self, cve):
        """ Search for and return CVE entry """
        return self.database.collection.find_one({"cve_id": cve}, manipulate=True)
