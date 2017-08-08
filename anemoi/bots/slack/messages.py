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

from collections import namedtuple, Iterable

from anemoi.utils.decorators import memoized

##########################################################################
# Classes
##########################################################################

MESSAGE_FIELDS = ['bot_id', 'channel', 'source_team', 'team', 'text', 'ts', 'type', 'user', 'event_ts', 'subtype']
MessageBase = namedtuple('MessageBase', ' '.join(MESSAGE_FIELDS))


class SlackMessage(MessageBase):
    """
    Class to encapsulate basic Slack message attributes along with additional
    message related functionality.
    """

    @property
    def _is_for_bot(self):
        bot_identifier = '<@{}>'.format(self.bot_id)
        return bot_identifier in self.text

    @property
    def _asks_for_weather_currently(self):
        # TODO: replace with regular expressions
        text = self.text.lower()
        return self._is_for_bot and (
            'current weather' in text
            or 'weather now' in text
            or 'weather currently' in text
        )

    @property
    def _asks_for_weather_tomorrow(self):
        # TODO: replace with regular expressions
        text = self.text.lower()
        return self._is_for_bot and (
            'tomorrow weather' in text
            or 'weather tomorrow' in text
            or "tomorrow's weather" in text
        )

    @property
    def _asks_for_weather(self):
        return self._asks_for_weather_currently or self._asks_for_weather_tomorrow


class SlackMessageFactory(object):
    """
    Factory object for Slack communications of type 'message'
    """

    def __init__(self, bot_id):
        self.bot_id = bot_id

    def create(self, data):
        """
        Returns a new SlackMessage instance from supplied input dict.

        params:
            data: (dict) dict of communication item from Slack RTM service

        returns:
            SlackMessage
        """
        data.update({'bot_id': self.bot_id})
        for field in MESSAGE_FIELDS:
            if field not in data:
                data[field] = None

        return SlackMessage(**data)


class SlackCommsFactory(object):
    """
    Factory object for converting Slack communications to the appropriate
    message class instance based on the dict 'type' key
    """

    def __init__(self, bot_id):
        self.bot_id = bot_id

    @memoized
    def factories(self):
        return {
            'message': SlackMessageFactory(self.bot_id)
        }

    def _create(self, data):
        """
        Returns a new Slack communication instance from supplied input dict using
        the 'type' key to determine the correct factory to use.

        params:
            data: (dict) dict of communication item from Slack RTM service

        returns:
            SlackMessage or None
        """
        if data['type'] in self.factories:
            return self.factories[data['type']].create(data)

    def create(self, data):
        """
        Returns a new SlackMessage instance of list of instances from supplied
        dict or iterable.

        params:
            data: (dict or iterable) single or iterable of communication item from Slack RTM service

        returns:
            SlackMessage or list of SlackMessage or None
        """
        if isinstance(data, dict):
            return self._create(data)

        if isinstance(data, Iterable):
            return filter(lambda val: val is not None, [self._create(item) for item in data])

        raise TypeError('create accepts only iterable or dict instances')


##########################################################################
# Execution
##########################################################################

if __name__ == '__main__':
    pass
