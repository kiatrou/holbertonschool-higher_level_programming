#!/usr/bin/python3
"""
This function returns a list of available attributes
and methods of an object
"""


def lookup(obj):
    """
    This function returns a list of available attributes
    and methods of an object
    dir() function returns a list of all valid attributes and methods
    of an object — including inherited ones.
    """
    return (dir(obj))
