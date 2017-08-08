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

from anemoi.apis.dark_sky import DarkSky

##########################################################################
# Classes
##########################################################################

class TestDarkSky(TestCase):

    @skip('Not Implemented')
    def test_init(self):
        obj = DarkSky('foo')
        self.assertIsInstance(obj, DarkSky)

    @skip('Not Implemented')
    def test_api_unreachable(self):
        pass

    @skip('Not Implemented')
    def test_custom_exception(self):
        pass

    @skip('Not Implemented')
    def test_bad_zip(self):
        pass

##########################################################################
# Execution
##########################################################################

if __name__ == '__main__':
    pass
