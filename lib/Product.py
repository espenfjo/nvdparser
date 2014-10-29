import logging

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
                logger.error(e)
