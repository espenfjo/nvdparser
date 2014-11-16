from pymongo import MongoClient
from lib.Product import Transform


class MongoDB(object):
    def __init__(self, nvd):
        self.nvd = nvd
        self.config = nvd.config
        client = MongoClient(self.config.mongo_host)
        db = client.cve
        db.add_son_manipulator(Transform())
        self.collection = db.cvedetails
