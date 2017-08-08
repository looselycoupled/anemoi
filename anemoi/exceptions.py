# anemoi.exceptions
# Custom exceptions for error handling and control flow
#
# Author:   Allen Leis <allen.leis@gmail.com>
# Created:  timestamp
#
# Copyright (C) 2017 Allen Leis
# For license information, see LICENSE
#
# ID: exceptions.py [] allen.leis@gmail.com $

"""
Custom exceptions for error handling and control flow
"""

##########################################################################
# Exception Classes
##########################################################################

class APIException(Exception):
    pass

class DarkSkyException(APIException):
    pass

class DarkSkyRateLimitException(DarkSkyException):
    pass

class DarkSkyInvalidResponseException(DarkSkyException):
    pass

class DarkSkyUnknownZipException(DarkSkyException):
    pass

class SlackException(Exception):
    pass


##########################################################################
# Execution
##########################################################################

if __name__ == '__main__':
    pass
