#!/usr/bin/python3
"""
This script demonstrates how to serialize a Python dictionary to XML
and deserialize XML back into a Python dictionary using ElementTree.
"""

import xml.etree.ElementTree as ET  # Import the XML processing module


def serialize_to_xml(dictionary, filename):
    """
    Serializes a Python dictionary into an XML file.

    Args:
        dictionary (dict): The dictionary to serialize.
        filename (str): The filename to write the XML to.

    Returns:
        bool: True if successful, False if any error occurs.
    """
    try:
        # Create the root element of the XML document
        root = ET.Element("data")

        # Add each key-value pair as a child element
        for key, value in dictionary.items():
            # Each key becomes a tag; value becomes the text inside the tag
            child = ET.SubElement(root, key)
            child.text = str(value)  # Ensure value is stored as a string

        # Create an ElementTree object from the root
        tree = ET.ElementTree(root)

        # Write the XML to file, with UTF-8 encoding and XML declaration
        tree.write(filename, encoding='utf-8', xml_declaration=True)

        return True  # Success
    except Exception:
        return False  # Something went wrong


def deserialize_from_xml(filename):
    """
    Deserializes an XML file back into a Python dictionary.

    Args:
        filename (str): The XML file to read from.

    Returns:
        dict: The reconstructed dictionary, or None if an error occurs.
    """
    try:
        # Parse the XML file and get the root element
        tree = ET.parse(filename)
        root = tree.getroot()

        result = {}  # The dictionary we will build and return

        # Loop through each child of the root element
        for child in root:
            text = child.text  # This is the string value from the XML

            # Try to convert it back to its original type
            if text == "True":
                result[child.tag] = True
            elif text == "False":
                result[child.tag] = False
            elif text.isdigit():
                result[child.tag] = int(text)  # Convert to integer
            else:
                try:
                    result[child.tag] = float(text)  # Try float conversion
                except ValueError:
                    result[child.tag] = text  # Leave it as a string

        return result  # Return the reconstructed dictionary
    except Exception:
        return None  # Return None if anything fails
