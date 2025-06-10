#!/usr/bin/python3
"""
This function returns a Python data structure represented
by a JSON string
"""

import json


def from_json_string(my_str):
    """
    json loads - does the opposite of dumps
    takes a single argument (the JSON string) and returns a python object
    """
    python_obj = json.loads(my_str)
    return (python_obj)
