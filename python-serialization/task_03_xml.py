#!/usr/bin/python3
"""
This script demonstrates how to serialize a Python dictionary to XML
and deserialize XML back into a Python dictionary using ElementTree.
"""

import xml.etree.ElementTree as ET  # Import the XML processing module


def serialize_to_xml(dictionary, filename):
    try:
        root = ET.Element("data")

        for key, value in dictionary.items():
            child = ET.SubElement(root, key)
            child.text = str(value)

            # Add type as an attribute
            if isinstance(value, bool):
                child.set("type", "bool")
            elif isinstance(value, int):
                child.set("type", "int")
            elif isinstance(value, float):
                child.set("type", "float")
            else:
                child.set("type", "str")

        tree = ET.ElementTree(root)
        tree.write(filename, encoding='utf-8', xml_declaration=True)
        return True
    except Exception:
        return False


def deserialize_from_xml(filename):
    try:
        tree = ET.parse(filename)
        root = tree.getroot()
        result = {}

        for child in root:
            type_attr = child.get("type")
            text = child.text

            # Convert based on stored type
            if type_attr == "int":
                result[child.tag] = int(text)
            elif type_attr == "float":
                result[child.tag] = float(text)
            elif type_attr == "bool":
                result[child.tag] = True if text == "True" else False
            else:
                result[child.tag] = text

        return result
    except Exception:
        return None
