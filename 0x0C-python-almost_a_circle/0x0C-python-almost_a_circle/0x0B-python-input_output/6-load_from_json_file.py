#!/usr/bin/python3
"""Module for loading an object from a JSON file."""
import json


def load_from_json_file(filename):
    """
    Creates an Object from a "JSON file".

    Args:
        filename (str): The name of the JSON file to load the object from.

    Returns:
        object: The Python object created from the JSON file.
    """
    with open(filename, 'r', encoding='utf-8') as file:
        return json.load(file)
