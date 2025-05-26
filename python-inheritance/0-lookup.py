#!/usr/bin/python3
"""
This function returns a list of available attributes
and methods of an object
"""


def lookup(obj):
    """
    This function returns a list of available attributes
    and methods of an object
    __dict__ is a built-in attribute that returns a dictionary representing
    the namespace (all attributes and their values) of an object or class.
    """
    return (obj.__dict__)
