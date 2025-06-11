#!/usr/bin/python3
"""
This is a function that returns a dictionary description with simlpe
data structures for JSON serialisation of an object
"""


def class_to_json(obj):
    """
    obj.__dict__ is a special attribute in Python that stores all the
    instance attributes of an object as a dictionary.
    """
    return (obj.__dict__)
