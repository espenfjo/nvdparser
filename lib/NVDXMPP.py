import datetime
import re
import sleekxmpp

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

        # The message event is triggered whenever a message
        # stanza is received. Be aware that that includes
        # MUC messages and error messages.
        self.add_event_handler('message', self.message)


    def run(self):
        self.register_plugin('xep_0030') # Service Discovery
        self.register_plugin('xep_0199') # Ping
        self.register_plugin('xep_0045') # Room

        if self.connect(('chat.basefarm.no', 5222)):
            self.process(block=True)
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
        room = self.plugin['xep_0045'].joinMUC(self.room,
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
            rm = re.search('CVE-[0-9]{4}-[0-9]{4,10}', msg['body'])
            cve = rm.group(0)
            self.logger.info("Searching for: {}".format(cve))
            vulnerability = self.nvd.find_cve(cve)
            if not vulnerability:
                message = "No information found for {}".format(cve)
                self.send_message(mto=msg['from'].bare,
                                  mbody=message,
                                  mtype='groupchat')
                return 0
            url = "{}{}".format(self.config.cveurl, vulnerability['cve_id'])
            message = "{} cvss={} vector={} vendor={} product={}: {} ( {} )".format(vulnerability['cve_id'],
                                                                               vulnerability['vulnerability']['cvss'],
                                                                               vulnerability['vulnerability']['vector'],
                                                                               vulnerability['vulnerability']['product'][0]['vendor'],
                                                                               vulnerability['vulnerability']['product'][0]['product'],
                                                                               vulnerability['vulnerability']['summary'],
                                                                               url)

        if message:
            self.send_message(mto=msg['from'].bare, mbody=message, mtype='groupchat')


    def updated(self, vulnerability):
        """ Send an CVE update message to the room """

        if vulnerability['cvss'] < self.config.cvssmin:
            return

        if not vulnerability['product'] or not vulnerability['product'][0]:
             vulnerability['product'] = []
             vulnerability['product'].append({
                 "vendor":None,
                 "product":None,
                 "version":None
             })
        url = "{}{}".format(self.config.cveurl, vulnerability['cve_id'])
        message = "[UPDATE] {} cvss={} vector={} vendor={} product={}: {} {}".format(vulnerability['cve_id'],
                                                                                     vulnerability['cvss'],
                                                                                     vulnerability['vector'],
                                                                                     vulnerability['product'][0]['vendor'],
                                                                                     vulnerability['product'][0]['product'],
                                                                                     vulnerability['summary'],
                                                                                     url)

        self.send_message(mto=self.room, mbody=message, mtype='groupchat')

    def new(self, vulnerability):
        """ Send a CVE to the room """


        if vulnerability['cvss'] < self.config.cvssmin:
            return
        if not vulnerability['product'] or not vulnerability['product'][0]:
             vulnerability['product'] = []
             vulnerability['product'].append({
                 "vendor":None,
                 "product":None,
                 "version":None
             })

        message = "[NEW] {} cvss={} vector={} vendor={} product={}: {} ( {} )".format(vulnerability['cve_id'],
                                                    vulnerability['cvss'],
                                                    vulnerability['vector'],
                                                    vulnerability['product'][0]['vendor'],
                                                    vulnerability['product'][0]['product'],
                                                    vulnerability['summary'],
                                                    vulnerability['url'])
        self.send_message(mto=self.room, mbody=message, mtype='groupchat')
