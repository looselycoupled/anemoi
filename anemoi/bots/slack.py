# anemoi.bots.slack
# module description
#
# Author:   Allen Leis <allen.leis@gmail.com>
# Created:  timestamp
#
# Copyright (C) 2017 Allen Leis
# For license information, see LICENSE
#
# ID: slack.py [] allen.leis@gmail.com $

"""
module description
"""

##########################################################################
# Imports
##########################################################################

import time
from pprint import pprint

from slackclient import SlackClient

from anemoi.utils.mixins import LoggableMixin
from anemoi.version import get_version

##########################################################################
# Classes
##########################################################################

class SlackBot(LoggableMixin):

    def __init__(self, access_token, bot_id, *args, **kwargs):
        self.access_token = access_token
        self.bot_id = bot_id
        super(SlackBot, self).__init__(*args, **kwargs)

    def start(self):
        self.logger.info('SlackBot v{} starting up with bot ID: {}'.format(
            get_version(),
            self.bot_id
        ))
        self.listen()

    def _filter_messages(self, data):
        return filter(lambda item: 'type' in item and item['type'] == 'message', data)


    def listen(self):

        sc = SlackClient(self.access_token)

        if sc.rtm_connect():
            while True:

                incoming = sc.rtm_read()
                if incoming:
                    pprint(self._filter_messages(incoming))
                    print('-' * 50)
                time.sleep(1)
        else:
            print "Connection Failed, invalid token?"

##########################################################################
# Execution
##########################################################################

if __name__ == '__main__':
    pass
