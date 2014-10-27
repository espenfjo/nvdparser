from pymongo import MongoClient

class mongodb(object):
    def __init__(self, nvd):
        self.nvd = nvd
        self.config = nvd.config
        client = MongoClient(self.config.mongo_host)
        db = client.cve
        self.collection = db.cvedetails
