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



##########################################################################
# Decorators
##########################################################################

def rate_limit(limit, period):
    """
    Limits the amount of times the decorated function may be called within
    a given time period.

    As an example or first iteration the period is assumed to be second, minute,
    hour, day, or month.  Ultimately we will need something that
    we can convert to a datetime.timespan so that we can do something more
    realistic such as "5 minutes"

    params:
        limit: (int) the maximum number of times the function may be called
            within the period of time
        period: {hour, minute, day, month} the period of time we are looking at to limit
            executions

    """
    def decorator(function):
        # TODO: develop actual rate limiting using limit/period

        def wrapper(*args, **kwargs):
            return function(*args, **kwargs)
        return wrapper

    return decorator

##########################################################################
# Execution
##########################################################################

if __name__ == '__main__':
    pass
