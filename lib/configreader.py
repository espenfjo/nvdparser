from configobj import ConfigObj
from configobj import ParseError
import logging
import sys
import os


def parse_config(configfile):
    """Parse a configuration file and create a Configuration
    object which will store all configuration"""

    if os.path.isfile(configfile):
        try:
            config = ConfigObj(configfile)
            return config
        except ParseError as e:
            logging.error("Cannot parse configuration file: {}".format(e))
            sys.exit(0)
    else:
        logging.error("Configuration file {} does not exist".format(configfile))
