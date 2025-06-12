#!/usr/bin/python3
"""
This is a basic serialization module
"""

import json


def serialization_and_save_to_file(data, filename):
    """
    since this is being saved into a file, need to use dump
    w - opening the file for writing (automatically creates
    a new file if it doesn't exist)
    """
    with open(filename, 'w', encoding="utf-8") as file:
        json.dump(data, file)


def load_and_deserialize(filename):
    """
    since this being loaded from a file, need to use load
    r - opening the file for reading
    """
    with open(filename, 'r', encoding="utf-8") as file:
        python_object = json.load(file)
        return (python_object)
