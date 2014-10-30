import logging
from pymongo.son_manipulator import SONManipulator

class Product(object):
    def __init__(self, cpe=None):
        self.vendor = None
        self.product = None
        self.version = None
        if cpe:
            try:
                self.vendor  = cpe.split(':')[2]
                self.product = cpe.split(':')[3]
                self.version = cpe.split(':')[4]
            except IndexError as e:
                logger = logging.getLogger("NVD")
                logger.error("{}: {}".format(cpe, e))


class Transform(SONManipulator):
    """
    Transform the Product objects into Mongo eatable dicts, and back
    """
    def transform_incoming(self, son, collection):
        """
        Convert a Product object into a Mongo/JSON object
        """
        if isinstance(son, dict):
            for (key, value) in son.items():
                if isinstance(value, dict):
                    son[key] = self.transform_incoming(value, collection)
                elif isinstance(value, list):
                    son[key] = self.transform_incoming(value, collection)
        elif isinstance(son, list):
            for (idx, item) in enumerate(son):
                if isinstance(item, Product):
                    son[idx] = item.__dict__
                    son[idx]['_type'] = 'product'
                elif isinstance(item, dict):
                    son[idx] = self.transform_incoming(item, collection)
                elif isinstance(item, list):
                    son[idx] = self.transform_incoming(item, collection)

        return son

    def transform_outgoing(self, son, collection):
        """
        Convert a MongoDB JSON/Dict into a Product object
        """
        for (key, value) in son.items():
            if isinstance(value, dict):
                if "product" in value and isinstance(value["product"], list):
                    for (idx, product) in enumerate(value['product']):
                        if '_type' in product and product['_type'] == 'product':
                            product_obj = Product()
                            product_obj.vendor  = product['vendor']
                            product_obj.product = product['product']
                            product_obj.version = product['version']
                            value['product'][idx] = product_obj
                            son[key] = value
                else:
                    son[key] = self.transform_incoming(value, collection)

        return son
