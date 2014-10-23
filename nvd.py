"""
...
"""
import lib._nvd as _nvd
import argparse
import logging
import urllib2
import sqlite3
import os
import time


def parse_arguments():

    parser = argparse.ArgumentParser(formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('-t', '--time',
                        help="How old (in hours) should the XML be before downloading a new version",
                        default=1)
    parser.add_argument('-f', '--force',
                        help="Always download a new XML",
                        action="store_true")
    parser.add_argument('-x', '--xml',
                        help="NVD XML file", default='recent.xml',)
    parser.add_argument('-d', '--debug',
                        help='Print lots of debugging statements',
                        action="store_const", dest="loglevel", const=logging.DEBUG,
                        default=logging.WARNING)
    parser.add_argument('-v', '--verbose',
                        help='Be verbose',
                        action="store_const", dest="loglevel", const=logging.INFO)

    args = parser.parse_args()
    return args


def parse_nvd(xml, db):
    """ Parse the XML and insert the CVE IDs into the database """

    nvd_data = _nvd.CreateFromDocument(xml)
    for entry in nvd_data.entry:
        vendor = ""
        products = []
        score = None
        vector = None
        if "REJECT" in entry.summary:
            continue
        if entry.vulnerable_software_list:
            product_list = entry.vulnerable_software_list.product
            for p in product_list:
                vendor = p.split(':')[2]
                product = p.split(':')[3]
                version = p.split(':')[4]
                products.append("{} {}-{}".format(vendor, product, version))
        cve = entry.cve_id
        date = entry.published_datetime
        summary = entry.summary

        if entry.cvss:
            cvss_list = entry.cvss.base_metrics
        for cvss in cvss_list:
            score = cvss.score
            vector = cvss.access_vector.value()

        logging.debug("Inserting {} into DB".format(cve))
        status = db.execute("INSERT INTO cvedetails (cve) VALUES ('{}')".format(cve))

        logging.info("{} {} {} {} {}".format(cve, score, " ".join(products), date, summary))


def download_if_needed():
    """ Downloads a new and updated NVD recent XML if needed """
    request = urllib2.Request('http://static.nvd.nist.gov/feeds/xml/cve/nvdcve-2.0-Recent.xml')
    try:
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
    if os.path.exists(args.xml):
        logging.debug("Last-Modified of the remote XML: {}".format(modified))
        logging.debug("{} age: {}".format(args.xml, time.ctime(os.path.getmtime(args.xml))))
        if os.path.isfile(args.xml):
            if os.path.getmtime(args.xml) >= modified_time:
                if args.force:
                    logging.debug("Local XML is unchanged from remote. But forcing download")
                else:
                    logging.debug("Local XML is unchanged from remote. Skipping download")
                    return 0

    with open(args.xml, 'w') as f:
        f.write(response.read())
    mtime = int(modified_time)
    os.utime(args.xml, (0, mtime))
    return 1


def init_db():
    """ Initialise the database """

    db_file = 'cve.db'
    create = 0
    if not os.path.exists(db_file):
        create = 1

    conn = sqlite3.connect(db_file)
    c = conn.cursor()
    if create:
        logging.debug("No database exists. Creating {}".format(db_file))
        c.execute('''CREATE TABLE cvedetails (id INTEGER PRIMARY KEY, cve TEXT)''')
        # c.execute('''CREATE UNIQUE INDEX cve_idx ON cvedetails(cve)''')

    return (c, conn)

args = parse_arguments()
logging.basicConfig(level=args.loglevel)

(db, conn) = init_db()

if download_if_needed():
    xml = open(args.xml, 'r').read()
    parse_nvd(xml, db)
    conn.commit()
else:
    logging.info("XML is unchanged. Skipping parse and import")

conn.close()
