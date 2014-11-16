# pylint: disable-msg=C0103

"""
...
"""
import argparse
import logging

from lib.NVD import NVD
from lib.configreader import parse_config
from lib.NVDXMPP import NVDXMPP


def read_config():
    """ Parse CLI arguments, and parse configuration file """

    parser = argparse.ArgumentParser(formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('-c', '--config',
                        help="Configuration file", default="nvd.conf", type=str)
    args, remaining_argv = parser.parse_known_args()

    parser.add_argument('-t', '--time',
                        help="How old (in hours) should the XML be before downloading a new version",
                        default=1)
    parser.add_argument('-u', '--username',
                        help="XMPP username")
    parser.add_argument('-p', '--password',
                        help="XMPP password")
    parser.add_argument('-r', '--xmpproom',
                        help="XMPP chat room")
    parser.add_argument('-n', '--xmppnick',
                        help="XMPP nick")
    parser.add_argument('-f', '--force',
                        help="Always download a new XML",
                        action="store_true")
    parser.add_argument('-i', '--importxml',
                        help="Import XML into the database")
    parser.add_argument('-C', '--cvssmin',
                        help="Always download a new XML",
                        action="store_true")
    parser.add_argument('-d', '--debug',
                        help='Print lots of debugging statements', action="count")
    parser.add_argument('-v', '--verbose',
                        help='Be verbose',
                        action="store_const", dest="loglevel", const=logging.INFO, default=logging.WARNING)

    config = parse_config(args.config)
    parser.set_defaults(**config)
    args = parser.parse_args(remaining_argv)
    return args


def setup_logging():
    """ Configures logging of main NVD and XMPP stuff"""

    logging.basicConfig(format="%(asctime)s %(name)s %(levelname)s\t%(message)s", datefmt="%Y-%m-%d %H:%M:%S")
    logger = logging.getLogger("NVD")

    if config.debug and config.debug > 0:
        config.loglevel = logging.DEBUG

    logger.setLevel(config.loglevel)
    xmpplogger = logging.getLogger("sleekxmpp")

    if config.debug:
        if config.debug == 1:
            xmpplogger.setLevel(logging.INFO)
        elif config.debug >= 2:
            xmpplogger.setLevel(logging.DEBUG)


config = read_config()
setup_logging()

nvd = NVD(config)
