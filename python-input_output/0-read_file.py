#!/usr/bin/python3
"""
This reads a file and prints it to the standard output
"""


def read_file(filename=""):
    """
    Using the with statement ensures that setup and takedown is
    automatically done
    """
    with open(filename, encoding="utf-8") as file:
        contents = file.read()
