# package.module
# module description
#
# Author:   Allen Leis <allen.leis@gmail.com>
# Created:  timestamp
#
# Copyright (C) 2017 Allen Leis
# For license information, see LICENSE
#
# ID: filename.py [] allen.leis@gmail.com $

"""
module description
"""

##########################################################################
# Imports
##########################################################################

from unittest import skip, TestCase
from mock import patch, Mock, MagicMock
from slackclient import SlackClient

from anemoi.bots.slack import SlackBot
from anemoi.exceptions import *

##########################################################################
# Classes
##########################################################################

class TestSlackBot(TestCase):

    @skip('Not Implemented')
    def test_init(self):
        obj = SlackBot('foo', 'foo', 'foo')
        self.assertIsInstance(obj, SlackBot)

    @skip('Not Implemented')
    def test_filter_messages(self):
        """
        tests ability to correctly filter for message events
        """
        pass

    @skip('Not Implemented')
    def test_filter_messages_empty_data(self):
        """
        tests ability process an empty list
        """
        pass

    @skip('Not Implemented')
    def test_filter_messages_non_message(self):
        """
        tests ability to filter out list of only non message events
        """
        pass

    def test_start_calls_listen(self):
        """
        tests that start method should call listen
        """
        obj = SlackBot('foo', 'foo', 'foo')

        mocked_call = MagicMock()
        obj.listen = mocked_call

        obj.start()
        mocked_call.assert_called_once()

    def test_reply_raises_exc(self):
        """
        tests that reply will raise SlackBadResponse if api_call returns bad response
        """
        obj = SlackBot('foo', 'foo', 'foo')

        mocked_call = MagicMock()
        mocked_call.api_call.return_value = {'ok': False}
        obj.client = mocked_call

        with self.assertRaises(SlackBadResponse):
            obj.reply('channel', 'content')


##########################################################################
# Execution
##########################################################################

if __name__ == '__main__':
    pass
