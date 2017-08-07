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
import signal
from pprint import pprint
from collections import namedtuple

from slackclient import SlackClient

from anemoi.utils.mixins import LoggableMixin
from anemoi.version import get_version
from .messages import SlackCommsFactory


##########################################################################
# Classes
##########################################################################

class SlackBot(LoggableMixin):

    def __init__(self, access_token, bot_id, *args, **kwargs):
        self.access_token = access_token
        self.bot_id = bot_id
        self.message_factory = SlackCommsFactory(self.bot_id)
        self._shutdown_sentinel = False
        signal.signal(signal.SIGINT, self.request_shutdown)
        super(SlackBot, self).__init__(*args, **kwargs)

    def start(self):
        self.logger.info('SlackBot v{} starting up with bot ID: {}'.format(
            get_version(),
            self.bot_id
        ))
        self.listen()

    def request_shutdown(self, *args):
        self.logger.info('SlackBot shutdown has been requested')
        self._shutdown_sentinel = True

    def _filter_messages(self, data):
        items = filter(lambda item: 'type' in item and item['type'] == 'message', data)
        # print('items', items)

        messages = self.message_factory.create(items)
        # print('messages', messages)

        weather_requests = [msg for msg in messages if msg._asks_for_weather]
        # print('weather_requests', weather_requests)

        return weather_requests

    def _handle_weather_current(self, msg):
        self.logger.info('Current weather request from {}'.format(msg.user))

    def _handle_weather_tomorrow(self, msg):
        self.logger.info('Tomorrow weather request from {}'.format(msg.user))

    def _handle_message(self, msg):
        if msg._asks_for_weather_currently:
            self._handle_weather_current(msg)

        if msg._asks_for_weather_tomorrow:
            self._handle_weather_tomorrow(msg)

    def listen(self):
        sc = SlackClient(self.access_token)

        if sc.rtm_connect():
            while not self._shutdown_sentinel:

                incoming = sc.rtm_read()
                if incoming:
                    entreaties = self._filter_messages(incoming)
                    [self._handle_message(msg) for msg in entreaties]

                time.sleep(1)
        else:
            print "Connection Failed, invalid token?"

##########################################################################
# Execution
##########################################################################

if __name__ == '__main__':
    pass
