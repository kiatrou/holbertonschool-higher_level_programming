#!/usr/bin/python3
"""
This module checks if an instance is the same as a specified class
"""


def is_same_class(obj, a_class):
    """
    This is a function that returns True if the object is exactly
    an instance of the specified class; otherwise False
    """
    return (type(obj) is a_class)
