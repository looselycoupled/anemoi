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
import requests

from anemoi.bots.slack.mixins import DarkSkyMixin
from anemoi.exceptions import *

##########################################################################
# Classes
##########################################################################

class TestDarkSkyMixin(TestCase):

    @skip('Not Implemented')
    def test_init(self):
        obj = TestDarkSkyMixin('foo')
        self.assertIsInstance(obj, TestDarkSkyMixin)

    @skip('Not Implemented')
    def test_init_adds_handler(self):
        """
        tests that __init__ was cause _handle_weather_message to be added to the handlers attribute
        """
        pass

    @skip('Not Implemented')
    def test_register_existing_attr(self):
        """
        tests _register correctly handles existing handlers attribute
        """
        pass

    @skip('Not Implemented')
    def test_register_nonexisting_attr(self):
        """
        tests _register correctly handles non-existing handlers attribute
        """
        pass

    @skip('Not Implemented')
    def test_handle_weather_message_calls_current(self):
        """
        tests that _handle_weather_message calls _handle_weather_current on correct message
        """
        pass

    @skip('Not Implemented')
    def test_handle_weather_message_calls_tomorrow(self):
        """
        tests that _handle_weather_message calls _handle_weather_tomorrow on correct message
        """
        pass

    @skip('Not Implemented')
    def test_handle_weather_current_calls_darksky_correctly(self):
        """
        tests that _handle_weather_current makes correct call to underlying DarkSky instance
        """
        pass

    @skip('Not Implemented')
    def test_handle_weather_tomorrow_calls_darksky_correctly(self):
        """
        tests that _handle_weather_tomorrow makes correct call to underlying DarkSky instance
        """
        pass


##########################################################################
# Execution
##########################################################################

if __name__ == '__main__':
    pass
