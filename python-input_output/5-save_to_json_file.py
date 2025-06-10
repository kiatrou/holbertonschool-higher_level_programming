#!/usr/bin/python3
"""
This function writes an Object to a text file,
using JSON representation
"""


import json


def save_to_json_file(my_obj, filename):
    """
    dump - the dump function takes two arguments, the Python
    and the file object
    """
    with open(filename, 'w', encoding="utf-8") as file:
        json.dump(my_obj, file)
