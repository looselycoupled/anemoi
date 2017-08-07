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

import sys
import os
sys.path.insert(0, os.getcwd())
from pprint import pprint

import requests

from anemoi.config import settings
from anemoi.exceptions import *
from anemoi.utils.decorators import rate_limit
from anemoi.utils.mixins import LoggableMixin


##########################################################################
# Module variables
##########################################################################

BASE_URL = 'https://api.darksky.net/forecast'

##########################################################################
# Classes
##########################################################################

class DarkSky(LoggableMixin):

    def __init__(self, access_token, *args, **kwargs):
        self.access_token = access_token
        super(DarkSky, self).__init__(*args, **kwargs)

    @property
    def request_params(self):
        return {
            'lang': 'en',
            'units': 'us',
            'exclude': []
        }

    def _construct_url(self, latitude, longitude):
        return '{}/{}/{},{}'.format(BASE_URL, self.access_token, latitude, longitude)

    def _request(self, latitude, longitude):
        url = self._construct_url(latitude, longitude)
        response = requests.get(url, params=self.request_params)
        try:
            response.raise_for_status()
        except requests.RequestException as e:
            self.logger.exception(e)
            raise DarkSkyException(e.message)

        return response.json()

    @rate_limit(limit=1000, period='month')
    def forecast(self, zip_code):
        latitude, longitude = 38.910353,-77.017739
        return self._request(latitude, longitude)

##########################################################################
# Execution
##########################################################################

if __name__ == '__main__':
    obj = DarkSky(settings.dark_sky.access_token)
    pprint(obj.forecast(20001))
