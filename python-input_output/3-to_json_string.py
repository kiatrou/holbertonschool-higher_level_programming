#!/usr/bin/python3
"""
This is a function that returns the JSON representation
of an object (string)
"""

import json


def to_json_string(my_obj):
    """
    json dumps is a function used to serialise a Python object
    into a JSON string - it takes a single argument (the python object)
    and returns a JSON string
    """
    json_string = json.dumps(my_obj)
    return (json_string)
