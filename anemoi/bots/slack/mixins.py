# anemoi.bots.mixins
# SlackBot mixin for DarkSky functionality
#
# Author:   Allen Leis <allen.leis@gmail.com>
# Created:  Mon Aug 07 21:19:50 2017 -0400
#
# Copyright (C) 2017 Allen Leis
# For license information, see LICENSE
#
# ID: mixins.py [] allen.leis@gmail.com $

"""
SlackBot mixin for DarkSky functionality
"""

##########################################################################
# Imports
##########################################################################

from anemoi.config import settings

from anemoi.apis.dark_sky import DarkSky

##########################################################################
# Classes
##########################################################################

class DarkSkyMixin(object):
    """
    Mixin to add dark sky response capabilities to the slack bot.

    Commentary: This was inelegantly done as it was refactored late in the
    process. Given more time I think this would be the right direction in order
    to keep the SlackBot client extensible.  (One would just have to add more mixins)
    """

    def __init__(self, darksky_access_token, *args, **kwargs):
        self.darksky = DarkSky(darksky_access_token)
        self._register()
        super(DarkSkyMixin, self).__init__(*args, **kwargs)

    def _register(self):
        if not hasattr(self, 'handlers'):
            self.handlers = []
        self.handlers.append(self._handle_weather_message)

    def _handle_weather_current(self, msg, zipcode=settings.zip_code):
        self.logger.info('Current weather request from {}'.format(msg.user))
        content = self.darksky.forecast(zipcode, now=True)
        self.reply(msg.channel, content)

    def _handle_weather_tomorrow(self, msg, zipcode=settings.zip_code):
        self.logger.info('Tomorrow weather request from {}'.format(msg.user))
        content = self.darksky.forecast(zipcode, now=False)
        self.reply(msg.channel, content)

    def _handle_weather_message(self, msg):
        if msg._asks_for_weather_currently:
            self._handle_weather_current(msg)

        if msg._asks_for_weather_tomorrow:
            self._handle_weather_tomorrow(msg)


##########################################################################
# Execution
##########################################################################

if __name__ == '__main__':
    pass
