#!/usr/bin/python3
"""
This is a script that adds all arguments to a Python list
and then saves them to a file
"""


import sys
import json
# Import the save_to_json_file and load_from_json_file functions
# using __import__ because the files have numeric prefixes
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file


"""
Check comments for notes
"""
# Using 1: ensures that only the arguments are used and not the filename,
# which is at index 0
# use sys.argv to accept input from terminal
arguments_being_added = sys.argv[1:]
# Define the filename where the list will be saved and loaded from
filename = "add_item.json"
try:
    # Try to load the existing list from the JSON file
    current_list = load_from_json_file(filename)
except FileNotFoundError:
    # create a new list if one isn't found
    current_list = []
# Add the new command-line arguments to the existing list
current_list.extend(arguments_being_added)
# Save the updated list back to the JSON file
save_to_json_file(current_list, filename)
