#!/usr/bin/python3
"""
This is a function that creates an object from a
"JSON file"
"""


import json


def load_from_json_file(filename):
    """
    load - takes a single argument, the file object, and
    returns a Python object
    """
    with open(filename, 'r', encoding="utf-8") as file:
        python_obj = json.load(file)
        return (python_obj)
