#!/usr/bin/python3
"""
This function appends a string at the end of a text file
and returns the number of characters added
"""


def append_write(filename="", text=""):
    """
    using a instead of w means it'll append the text file
    """
    with open(filename, 'a', encoding="utf-8") as file:
        result = file.write(text)
        return (result)
