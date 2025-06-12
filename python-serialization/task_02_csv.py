#!/usr/bin/python3
"""
The objective of this exercise is to gain experience in reading
data from one format (CSV) and converting it into another format
(JSON) using serialization techniques.
"""


import csv
import json


def convert_csv_to_json(csv_filename):
    """
    converts a csv file to a json file
    """
    try:
        with open(csv_filename, 'r', encoding="utf-8") as csvfile:
            data = list(csv.DictReader(csvfile))
        with open('data.json', 'w', encoding="utf-8") as jsonfile:
            json.dump(data, jsonfile)
        return (True)
    except Exception:
        return (False)
