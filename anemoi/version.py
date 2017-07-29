# anemoi.version
# Version related info
#
# Author:   Allen Leis <allen.leis@gmail.com>
# Created:  Sat Jul 29 14:21:42 2017 -0400
#
# Copyright (C) 2017
# For license information, see LICENSE.txt
#
# ID: version.py [] allen.leis@gmail.com $

"""
Version related info
"""

##########################################################################
# Configuration
##########################################################################

__version_info__ = {
    'major': 0,
    'minor': 0,
    'micro': 1,
    'releaselevel': 'final',
    'serial': 0,
}

##########################################################################
# Code
##########################################################################

def get_version(short=False):
    """
    Returns the version from the version info.
    """
    assert __version_info__['releaselevel'] in ('alpha', 'beta', 'final')
    vers = ["%(major)i.%(minor)i" % __version_info__, ]
    if __version_info__['micro']:
        vers.append(".%(micro)i" % __version_info__)
    if __version_info__['releaselevel'] != 'final' and not short:
        vers.append('%s%i' % (__version_info__['releaselevel'][0],
                              __version_info__['serial']))
    return ''.join(vers)
