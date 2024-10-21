#!/usr/bin/python3
"""Module for saving an object to a file in JSON format."""
import json


def save_to_json_file(my_obj, filename):
    """
    Writes an Object to a text file, using a JSON representation.

    Args:
        my_obj: The object to be saved to the file.
        filename (str): The name of the file to save the object to.
    """
    with open(filename, 'w', encoding='utf-8') as file:
        json.dump(my_obj, file)
