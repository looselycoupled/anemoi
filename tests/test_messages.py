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

from anemoi.bots.slack.messages import SlackMessage, SlackMessageFactory, SlackCommsFactory

##########################################################################
# Testing for Messages
##########################################################################

class TestMessages(TestCase):
    bot_id = 'UXXXXXXXX'

    def test_init(self):
        data = {
            'channel': 'G6LD97PHV',
            'source_team': 'T51H77538',
            'team': 'T51H77538',
            'text': '<@UXXXXXXXX> test',
            'ts': '1502140702.608441',
            'type': 'message',
            'user': 'UYYYYYYY',
            'bot_id': self.bot_id
        }
        obj = SlackMessage(**data)
        self.assertIsInstance(obj, SlackMessage)

    def test_is_for_bot_true(self):
        data = {
            'channel': 'G6LD97PHV',
            'source_team': 'T51H77538',
            'team': 'T51H77538',
            'text': '<@UXXXXXXXX> test',
            'ts': '1502140702.608441',
            'type': 'message',
            'user': 'UYYYYYYY',
            'bot_id': self.bot_id
        }
        obj = SlackMessage(**data)
        self.assertTrue(obj._is_for_bot)

    def test_is_for_bot_false(self):
        data = {
            'channel': 'G6LD97PHV',
            'source_team': 'T51H77538',
            'team': 'T51H77538',
            'text': '<@INCORRECT_VALUE> test',
            'ts': '1502140702.608441',
            'type': 'message',
            'user': 'UYYYYYYY',
            'bot_id': self.bot_id
        }
        obj = SlackMessage(**data)
        self.assertFalse(obj._is_for_bot)

    @skip('Not Implemented')
    def test_asks_for_weather_currently_true(self):
        pass

    @skip('Not Implemented')
    def test_asks_for_weather_currently_false(self):
        pass

    @skip('Not Implemented')
    def test_asks_for_weather_tomorrow_true(self):
        pass

    @skip('Not Implemented')
    def test_asks_for_weather_tomorrow_false(self):
        pass

    @skip('Not Implemented')
    def test_asks_for_weather_true(self):
        pass

    @skip('Not Implemented')
    def test_asks_for_weather_false(self):
        pass

##########################################################################
# Testing for TestMessageFactory
##########################################################################

class TestMessageFactory(TestCase):

    def setUp(self):
        self.samples = {
            'bot_id': 'UXXXXXXXX',
            'good_message': {
                'channel': 'G6LD97PHV',
                'source_team': 'T51H77538',
                'team': 'T51H77538',
                'text': '<@UXXXXXXXX> test',
                'ts': '1502140702.608441',
                'type': 'message',
                'user': 'UYYYYYYY',
                'bot_id': 'UXXXXXXXX'
            }
        }
        self.factory = SlackMessageFactory(self.samples['bot_id'])

    def test_init(self):
        self.assertIsInstance(self.factory, SlackMessageFactory)

    def test_creates_message(self):
        msg = self.factory.create(self.samples['good_message'])
        self.assertIsInstance(msg, SlackMessage)


##########################################################################
# Testing for TestCommsFactory
##########################################################################

class TestCommsFactory(TestCase):

    def setUp(self):
        self.samples = {
            'bot_id': 'UXXXXXXXX',
            'good_message': {
                'channel': 'G6LD97PHV',
                'source_team': 'T51H77538',
                'team': 'T51H77538',
                'text': '<@UXXXXXXXX> test',
                'ts': '1502140702.608441',
                'type': 'message',
                'user': 'UYYYYYYY',
                'bot_id': 'UXXXXXXXX'
            }
        }
        self.factory = SlackCommsFactory(self.samples['bot_id'])

    def test_init(self):
        self.assertIsInstance(self.factory, SlackCommsFactory)

    def test_creates_message(self):
        msg = self.factory.create(self.samples['good_message'])
        self.assertIsInstance(msg, SlackMessage)

    @skip('Not Implemented')
    def test_has_factories(self):
        pass

    @skip('Not Implemented')
    def test_throws_typeerror(self):
        pass



##########################################################################
# Execution
##########################################################################

if __name__ == '__main__':
    pass
