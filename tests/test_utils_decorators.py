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

from anemoi.utils.decorators import rate_limit
from anemoi.exceptions import *

##########################################################################
# Classes
##########################################################################

class TestRateLimit(TestCase):
    # TODO: add tests for rate limit (which is already fake)
    pass

##########################################################################
# Execution
##########################################################################

if __name__ == '__main__':
    pass
