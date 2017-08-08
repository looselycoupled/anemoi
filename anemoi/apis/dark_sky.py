# anemoi.apis.dark_sky
# Classes for interaction with the Dark Sky API
#
# Author:   Allen Leis <allen.leis@gmail.com>
# Created:  Mon Aug 07 01:54:53 2017 -0400
#
# Copyright (C) 2017 Allen Leis
# For license information, see LICENSE
#
# ID: dark_sky.py [] allen.leis@gmail.com $

"""
Classes for interaction with the Dark Sky API
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
from anemoi.utils.geo import zip_codes


##########################################################################
# Module variables
##########################################################################

BASE_URL = 'https://api.darksky.net/forecast'

##########################################################################
# Classes
##########################################################################

class DarkSky(LoggableMixin):

    BASE_URL = BASE_URL

    def __init__(self, access_token, *args, **kwargs):
        self.access_token = access_token
        self.zip_map = zip_codes()
        super(DarkSky, self).__init__(*args, **kwargs)

    @property
    def request_params(self):
        """
        Returns default request parameters as a dict
        """
        return {
            'lang': 'en',
            'units': 'us',
            'exclude': []
        }

    def _zip_to_coordinates(self, zip_code):
        """
        Returns a tuple of the lat/long values for a give zip code

        params:
            zip_code: (int or str) the requested zip code

        returns:
            str: the converted latitude
            str: the converted longitude
        """
        try:
            item = self.zip_map[int(zip_code)]
        except KeyError as e:
            raise DarkSkyUnknownZipException('Unknown zip code of {}'.format(zip_code))

        return item['latitude'], item['longitude']

    def _construct_url(self, latitude, longitude):
        """
        Returns a full request URL based on supplied lat/long

        params:
            latitude: (float) latitude for request
            longitude: (float) longitude for request

        returns:
            string: URL for API request
        """
        return '{}/{}/{},{}'.format(self.BASE_URL, self.access_token, latitude, longitude)

    def _request(self, latitude, longitude):
        """
        Performs actual API request with a given lat/long and returns json
        response as a dict

        params:
            latitude: (float) latitude for request
            longitude: (float) longitude for request

        returns:
            dict: converted api response from json string
        """
        url = self._construct_url(latitude, longitude)
        response = requests.get(url, params=self.request_params)
        try:
            response.raise_for_status()
        except requests.RequestException as e:
            self.logger.exception(e)
            raise DarkSkyException(e.message)

        return response.json()

    def _humanize_humidity(self, humidity):
        """
        Takes an number representing the humidity and returns a string
        characterizing how one would perceive it.
        """
        # TODO determine what input humidity feels like... may also need temp
        pass

    def _humanize_current(self, data):
        """
        Takes expected output from API and returns a string characterizing the
        current weather.

        params:
            data: (dict) response from dark sky api

        returns:
            string: human description of current conditions
        """
        # TODO: cleanup summary values such as "Drizzle"
        try:
            return 'It is currently {} and {} degrees outside.'.format(
                data['currently']['summary'],
                int(data['currently']['temperature']),
            )
        except KeyError as e:
            raise DarkSkyInvalidResponseException("Could not determine current forecast.")

    def _humanize_tomorrow(self, data):
        """
        Takes expected output from API and returns a string characterizing the
        forecast for tomorrow's weather.

        params:
            data: (dict) response from dark sky api

        returns:
            string: human description of future weather
        """
        try:
            return data['daily']['summary']
        except KeyError as e:
            raise DarkSkyInvalidResponseException("Could not determine tomorrow's forecast.")

    @rate_limit(limit=1000, period='month')
    def forecast(self, zip_code, now=True):
        """
        Returns the requested forecast based on supplied zip code.

        params:
            zip: (int) the zipcode to request
            now: (bool) whether to return current or tomorrow's conditions
        """
        latitude, longitude = self._zip_to_coordinates(zip_code)
        raw = self._request(latitude, longitude)

        if now:
            return self._humanize_current(raw)
        else:
            return self._humanize_tomorrow(raw)

##########################################################################
# Execution
##########################################################################

if __name__ == '__main__':
    obj = DarkSky(settings.dark_sky.access_token)
    print(obj.forecast(20001))
