#!/usr/bin/python3
"""
This module checks if an instance is the same as a specified class
"""


def is_same_class(obj, a_class):
    """
    This is a function that returns True if the object is exactly
    an instance of the specified class; otherwise False
    """
    if obj is isinstance(obj, int):
        return (True)
    elif obj is isinstance(obj, float):
        return (True)
    elif obj is isinstance(obj, str):
        return (True)
    else:
        return (False)
