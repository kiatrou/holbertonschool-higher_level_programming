#!/usr/bin/python3
"""
This function writes a string to a text file
and returns the number of characters written
"""


def write_file(filename="", text=""):
    """
    Note: write has a built-in function that counts characters
    Opening the file in w mode (write mode) in order to create/overwrite
    the contents of the file and used the standard encoding
    """
    with open(filename, 'w', encoding="utf-8") as file:
        result = file.write(text)
        return (result)
