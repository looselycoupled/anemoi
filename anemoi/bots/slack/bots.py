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
from collections import namedtuple

from slackclient import SlackClient
from concurrent.futures import ThreadPoolExecutor

from anemoi.utils.mixins import LoggableMixin
from anemoi.version import get_version
from anemoi.exceptions import SlackException
from .messages import SlackCommsFactory

from .mixins import DarkSkyMixin

##########################################################################
# Classes
##########################################################################

class SlackBot(LoggableMixin, DarkSkyMixin):
    """
    Basic Slack chat bot that can be extended by adding mixins.

    TODO: Clean up the way mixins register themselves.  Perhaps instead have
    a list of message handlers that respond to different message types.
    """

    def __init__(self, slack_access_token, slack_bot_id, *args, **kwargs):
        self.access_token = slack_access_token
        self.bot_id = slack_bot_id
        self.message_factory = SlackCommsFactory(self.bot_id)
        self._shutdown_sentinel = False
        signal.signal(signal.SIGINT, self.request_shutdown)
        super(SlackBot, self).__init__(*args, **kwargs)

    def start(self):
        """
        Public method to initiate the bot
        """
        self.logger.info('SlackBot v{} starting up with bot ID: {}'.format(
            get_version(),
            self.bot_id
        ))
        self.listen()

    def request_shutdown(self, *args):
        """
        Signal handler and public method to signal a shutdown of the bot
        """
        self.logger.info('SlackBot shutdown has been requested')
        self._shutdown_sentinel = True

    def _filter_messages(self, data):
        """
        Returns a list of message instances for known message types
        """
        items = filter(lambda item: 'type' in item and item['type'] == 'message', data)
        messages = self.message_factory.create(items)
        return messages

    def _process_message(self, msg):
        """
        Cycles through known message handlers in so that a message can be processed.  In
        this manner multiple requests could be handled in a single message from the user.
        """
        for handler in self.handlers:
            handler(msg)

    def reply(self, channel, content):
        """
        Public method to post back to the Slack team.  Used by mixins which
        actually respond to the various message types.
        """
        try:
            response = self.client.api_call(
                "chat.postMessage",
                channel=channel,
                text=content,
                as_user=True
            )
            if not response['ok']:
                self.logger.error('Error posting reply to channel')
        except Exception as e:
            self.logger.exception(e)

    def listen(self, concurrency=4):
        """
        Begins the process of listening for slack messages by connecting to the
        RTM api and responds to each request using a thread pool.
        """
        self.client = SlackClient(self.access_token)
        with ThreadPoolExecutor(max_workers=concurrency) as pool:

            if self.client.rtm_connect():
                while not self._shutdown_sentinel:

                    incoming = self.client.rtm_read()
                    if incoming:
                        entreaties = self._filter_messages(incoming)
                        for msg in entreaties:
                            pool.submit(self._process_message, msg)
                            # self._process_message(msg)

                    time.sleep(1)
            else:
                print "Connection Failed, invalid token?"

##########################################################################
# Execution
##########################################################################

if __name__ == '__main__':
    pass
