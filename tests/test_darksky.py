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

from anemoi.apis.dark_sky import DarkSky
from anemoi.exceptions import *

##########################################################################
# Classes
##########################################################################

class TestDarkSky(TestCase):

    @skip('Not Implemented')
    def test_init(self):
        obj = DarkSky('foo')
        self.assertIsInstance(obj, DarkSky)

    @skip('Not Implemented')
    def test_construct_url(self):
        """
        tests that darksky service URL is properly constructed
        """
        pass

    @skip('Not Implemented')
    @patch('requests.get')
    def test_bad_get_raises_custom_exception(self, mocked_get):
        """
        tests an HTTPError will be trapped and raise DarkSkyException
        """
        pass

    @skip('Not Implemented')
    def test_zip_to_coordinates_raises_custom_ex(self):
        """
        tests that errors with zipcode mapping will result in DarkSkyUnknownZipException
        """
        pass

    @skip('Not Implemented')
    def test_humanize_current_raises_custom_ex(self):
        """
        tests that KeyError in humanize_current raises DarkSkyInvalidResponseException
        """
        pass

    @skip('Not Implemented')
    def test_humanize_tomorrow_raises_custom_ex(self):
        """
        tests that KeyError in humanize_current raises DarkSkyInvalidResponseException
        """
        pass

    @skip('Not Implemented')
    def test_humanize_current(self):
        """
        tests that _humanize_current returns correct output
        """
        pass

    @skip('Not Implemented')
    def test_humanize_tomorrow(self):
        """
        tests that _humanize_tomorrow returns correct output
        """
        pass

    @skip('Not Implemented')
    def test_zip_to_coordinates(self):
        """
        tests that _zip_to_coordinates returns correct output for 20001
        """
        pass





##########################################################################
# Execution
##########################################################################

if __name__ == '__main__':
    pass
