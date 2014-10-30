import datetime
import re
import sleekxmpp
from lib.Vulnerability import Vulnerability
from lib.Product import Product

class NVDXMPP(sleekxmpp.ClientXMPP):
    """ XMPP Class """

    KEEP_ALIVE = 60

    def __init__(self, nvd):
        super(NVDXMPP, self).__init__(nvd.config.username, nvd.config.password)
        self.logger = nvd.logger
        self.config = nvd.config
        self.nvd = nvd
        self.room = self.config.xmpproom
        self.nick = self.config.xmppnick

        self.auto_reconnect = True

        # The session_start event will be triggered when
        # the bot establishes its connection with the server
        # and the XML streams are ready for use. We want to
        # listen for this event so that we we can initialize
        # our roster.
        self.add_event_handler('session_start', self.start)

        # The groupchat_message event is triggered whenever a message
        # stanza is received from any chat room. If you also also
        # register a handler for the 'message' event, MUC messages
        # will be processed by both handlers.
        self.add_event_handler('groupchat_message', self.message)


    def run(self):
        self.register_plugin('xep_0030') # Service Discovery
        self.register_plugin('xep_0199') # Ping
        self.register_plugin('xep_0045') # Room

        if self.connect():
            self.process(block=False)
            self.logger.debug("Disconnecting from jabber")
        else:
            self.logger.error('Unable to connect to jabber')

    def start(self, event):
        """
        Process the session_start event.

        Typical actions for the session_start event are
        requesting the roster and broadcasting an initial
        presence stanza.

        Arguments:
            event -- An empty dictionary. The session_start
                     event does not provide any additional
                     data.
        """
        self.send_presence()
        self.get_roster()
        self.plugin['xep_0045'].joinMUC(self.room,
                                        self.nick,
                                        wait=True)

    def message(self, msg):
        """
        Process incoming message stanzas. Be aware that this also
        includes MUC messages and error messages. It is usually
        a good idea to check the messages's type before processing
        or sending replies.

        Arguments:
            msg -- The received message stanza. See the documentation
                   for stanza objects and the Message stanza to see
                   how it may be used.
        """
        self.logger.debug("Got a message: {}".format(msg))
        if msg['mucnick'] == self.nick:
            return

        message = None
        if '!cve' in msg['body']:
            matcher = re.search(r'!cve \S+', msg['body'])
            search_string = matcher.group(0)
            self.logger.debug("Got search string: {}".format(search_string))
            cve_matcher = re.search(r'CVE-[0-9]{4}-[0-9]{4,10}', search_string)
            if not cve_matcher:
                message = "{} doesnt look like a CVE".format(search_string)
                self.say(message)
                return 0

            cve = cve_matcher.group(0)
            self.logger.info("Searching for: {}".format(cve))

            vulnerability = Vulnerability(self.nvd.find_cve(cve))

            if not vulnerability.cve_id:
                message = "No information found for {}".format(cve)
                self.say(message)
                return 0

            self.send_vulnerability(vulnerability)

    def updated(self, vulnerability):
        """
        Send an CVE update message to the room
        """

        if not vulnerability.cvss or vulnerability.cvss <= self.config.cvssmin:
            return

        self.send_vulnerability(vulnerability, vuln_type="UPDATE")

    def new(self, vulnerability):
        """
        Send a new CVE to the room
        """

        if not vulnerability.cvss or vulnerability.cvss <= self.config.cvssmin:
            return

        self.send_vulnerability(vulnerability, vuln_type="NEW")

    def send_vulnerability(self, vulnerability, vuln_type=""):
        """
        Send a CVE to the room
        """
        cve_url = "{}{}".format(self.config.cveurl, vulnerability.cve_id)

        if vuln_type != "":
            vuln_type = "[{}] ".format(vuln_type)


        message = "{}{} cvss={} vector={} vendor={} product={}: {} ( {} )".format(vuln_type,
                                                                                  vulnerability.cve_id,
                                                                                  vulnerability.cvss,
                                                                                  vulnerability.vector,
                                                                                  vulnerability.product[0].vendor,
                                                                                  vulnerability.product[0].product,
                                                                                  vulnerability.summary,
                                                                                  cve_url)
        self.say(message)

    def say(self, message):
        """
        Sends a message to the room
        """
        self.send_message(mto=self.room, mbody=message, mtype='groupchat')
