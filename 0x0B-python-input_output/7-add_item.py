#!/usr/bin/python3

import json

def save_to_json_file(my_obj, filename):
    """
    Save an object to a JSON file.

    Parameters:
    my_obj: The object to be serialized to JSON.
    filename: The name of the file where the JSON data will be saved.

    This function opens the specified file in write mode and writes the JSON
    representation of the given object to it, ensuring proper UTF-8 encoding.
    """
    with open(filename, "w", encoding="UTF-8") as f:
        json.dump(my_obj, f)
