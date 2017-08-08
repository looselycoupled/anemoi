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

from functools import wraps

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


def memoized(fget):
    """
    Return a property attribute for new-style classes that only calls its
    getter on the first access. The result is stored and on subsequent
    accesses is returned, preventing the need to call the getter any more.

    https://github.com/estebistec/python-memoized-property
    """
    attr_name = '_{0}'.format(fget.__name__)

    @wraps(fget)
    def fget_memoized(self):
        if not hasattr(self, attr_name):
            setattr(self, attr_name, fget(self))
        return getattr(self, attr_name)

    return property(fget_memoized)

##########################################################################
# Execution
##########################################################################

if __name__ == '__main__':
    pass
