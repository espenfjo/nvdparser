import logging
import httplib
import sys
import time
import urllib2

from lib.mongodb import mongodb
import lib._nvd as _nvd


class NVD(object):
    def __init__(self, config):
        self.config = config

        self.database = mongodb(self)

    def parse_nvd(self):
        """ Parse the XML and insert the CVE IDs into the database """
        logging.debug("Fetching XML from mongodb")
        mongo_xml = self.database.collection.find_one({"xml": {'$exists': True}})
        if not mongo_xml:
            logging.error("Could not find XML in MongoDB")
            return 0
        xml = mongo_xml['xml']['data']

        logging.info("Parsing XML data")
        nvd_data = _nvd.CreateFromDocument(xml)
        for entry in nvd_data.entry:
            vulnerability = {}
            if "REJECT" in entry.summary:
                continue
            if entry.vulnerable_software_list:
                vulnerability['product'] = []
                product_list = entry.vulnerable_software_list.product
                for product in product_list:
                    vulnerability['product'].append({
                        "vendor": product.split(':')[2],
                        "product": product.split(':')[3],
                        "version": product.split(':')[4]
                    })
            vulnerability['cve_id'] = entry.cve_id
            vulnerability['publish_date'] = str(entry.published_datetime)
            vulnerability['update_date'] = str(entry.last_modified_datetime)
            vulnerability['summary'] = entry.summary

            vulnerability['cvss'] = []
            if entry.cvss:
                cvss_list = entry.cvss.base_metrics
            for cvss in cvss_list:
                vulnerability['cvss'].append({
                    "score": cvss.score,
                    "vector": cvss.access_vector.value()
                })

            logging.debug("Inserting {} into DB".format(entry.cve_id))
            write_result = self.database.collection.update(
                {"cve_id": entry.cve_id},
                {"$set": {"vulnerability": vulnerability}},
                upsert=True
            )
            if write_result['nModified'] > 0:
                logging.info("{} has been updated".format(entry.cve_id))

    def download_if_needed(self):
        """ Downloads a new and updated NVD recent XML if needed """
        url = 'http://static.nvd.nist.gov/feeds/xml/cve/nvdcve-2.0-Recent.xml'
        request = urllib2.Request(url)
        request.get_method = lambda: 'HEAD'
        try:
            logging.debug("HEADing {}".format(url))
            response = urllib2.urlopen(request)
        except urllib2.HTTPError, e:
            logging.error('HTTPError = ' + str(e.code))
            sys.exit(1)
        except urllib2.URLError, e:
            logging.error('URLError = ' + str(e.reason))
            sys.exit(1)
        except httplib.HTTPException, e:
            logging.error('HTTPException')
            sys.exit(1)
        except Exception:
            import traceback
            logging.error('generic exception: ' + traceback.format_exc())
            sys.exit(1)

        modified = response.info().getheader('Last-Modified')
        modified_time = time.mktime(time.strptime(modified, '%a, %d %b %Y %H:%M:%S %Z'))
        logging.info("Last-Modified of the remote XML: {}".format(modified))

        logging.debug("Fetching XML from mongodb")
        mongo_xml = self.database.collection.find_one({"xml": {'$exists': True}})
        if mongo_xml:
            logging.info("Local XML age: {}".format(time.ctime(mongo_xml['xml']['mtime'])))
            if mongo_xml['xml']['mtime'] >= modified_time:
                if self.config.force:
                    logging.info("Local XML is unchanged from remote. But forcing download")
                else:
                    logging.info("Local XML is unchanged from remote. Skipping download")
                    return 0

        request.get_method = lambda: 'GET'
        try:
            logging.debug("GETing {}".format(url))
            response = urllib2.urlopen(request)
        except urllib2.HTTPError, e:
            logging.error('HTTPError = ' + str(e.code))
            sys.exit(1)
        except urllib2.URLError, e:
            logging.error('URLError = ' + str(e.reason))
            sys.exit(1)
        except httplib.HTTPException, e:
            logging.error('HTTPException')
            sys.exit(1)
        except Exception:
            import traceback
            logging.error('generic exception: ' + traceback.format_exc())
            sys.exit(1)

        xml = {
            "xml": {
                "mtime": modified_time,
                "data": response.read()
            }
        }
        self.database.collection.update({"xml": {'$exists': True}}, xml, upsert=True)
        return 1
