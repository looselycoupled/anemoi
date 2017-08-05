# anemoi.config
# primary configuration module for Anemoi project
#
# See http://confire.readthedocs.io/en/latest/ for usage and documentation
#
# Author:   Allen Leis <allen.leis@gmail.com>
# Created:  Sat Aug 05 14:39:18 2017 -0400
#
# Copyright (C) 2017 Allen Leis
# For license information, see LICENSE
#
# ID: config.py [] allen.leis@gmail.com $

"""
primary configuration module for Anemoi project
"""

##########################################################################
## Imports
##########################################################################

from confire import Configuration
from confire import environ_setting
import os

##########################################################################
## Classes
##########################################################################

class SlackConfiguration(Configuration):
    access_token = ""

class DarkSkyConfiguration(Configuration):
    access_token = ""

class DefaultConfiguration(Configuration):

    CONF_PATHS = [
        'conf/settings.{}.yaml'.format(os.getenv('ANEMOI_ENV', 'development')),
    ]

    slack = SlackConfiguration()
    dark_sky = DarkSkyConfiguration()

    zip_code = 20001


settings = DefaultConfiguration.load()
