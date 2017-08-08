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

from pprint import pprint

from anemoi.config import settings

from anemoi.bots.slack import SlackBot
from anemoi.bots.slack.messages import SlackCommsFactory

##########################################################################
# Classes
##########################################################################


##########################################################################
# Execution
##########################################################################

if __name__ == '__main__':
    bot = SlackBot(settings.slack.access_token, settings.slack.bot_id)
    bot.start()
