#!/usr/bin/python3

import json

def save_to_json_file(my_obj, filename):
    """ 
    Save an object to a JSON file.

    Args:
        my_obj: The object to serialize to JSON.
        filename: The name of the file to save the JSON data.

    This function opens the specified file in write mode and saves the 
    JSON representation of the object. The file is encoded in UTF-8.
    """
    with open(filename, "w", encoding="UTF-8") as f:
        json.dump(my_obj, f)
