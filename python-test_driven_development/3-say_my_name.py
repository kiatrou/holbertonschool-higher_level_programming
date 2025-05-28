#!/usr/bin/python3
"""
This is a function that prints out a first and last name.
"""


def say_my_name(first_name, last_name=""):
    """
    This function takes in two arguments - first name and last name
    last name will default to empty string if not filled
    prints "My name is <firtst name> <last name>
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print(f"My name is {first_name} {last_name}")
