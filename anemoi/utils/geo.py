# anemoi.utils.geo
# Provides zipcode and geographic data
#
# Author:   Allen Leis <allen.leis@gmail.com>
# Created:  Mon Aug 07 01:58:32 2017 -0400
#
# Copyright (C) 2017 Allen Leis
# For license information, see LICENSE
#
# ID: geo.py [] allen.leis@gmail.com $

"""
Provides zipcode and geographic data
"""

##########################################################################
# Imports
##########################################################################

import os

import unicodecsv as csv

##########################################################################
# Functions
##########################################################################

def zip_codes():
    """
    Returns a dict of zip code to lat/long mappings based off of the CSV found
    at https://gist.github.com/erichurst/7882666 (2013)
    """
    filename = 'zip_lat_long.csv'
    path = os.path.join(os.getcwd(), 'fixtures', 'csv', filename)
    data = {}
    with open(path) as f:
        reader = csv.DictReader(f)
        for row in reader:
            data[int(row['ZIP'])] = {
                'latitude': row['LAT'].strip(),
                'longitude': row['LNG'].strip(),
            }
    return data

def zip2geo(zip_code):
    """
    Returns a dict of lat/long info for supplied zip code
    """
    return zip_codes()[zip_code]

##########################################################################
# Execution
##########################################################################

if __name__ == '__main__':
    print zip2geo(20001)
