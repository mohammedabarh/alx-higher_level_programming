#!/usr/bin/python3
"""
This module defines a function to return the JSON representation
of an object (string).
"""


def to_json_string(my_obj):
    """Return the JSON representation of an object.

    Args:
        my_obj: The object to convert to JSON format.

    Returns:
        str: JSON representation of the object.
    """
    json_repr = ""

    if isinstance(my_obj, dict):
        json_repr += "{"
        json_repr += ", ".join(
            f'"{key}": {to_json_string(value)}' for key, value in my_obj.items()
        )
        json_repr += "}"
    elif isinstance(my_obj, list):
        json_repr += "["
        json_repr += ", ".join(to_json_string(item) for item in my_obj)
        json_repr += "]"
    elif isinstance(my_obj, str):
        json_repr = f'"{my_obj}"'
    elif isinstance(my_obj, (int, float)):
        json_repr = str(my_obj)
    elif isinstance(my_obj, bool):
        json_repr = "true" if my_obj else "false"
    else:
        json_repr = "null"  # Handle None

    return json_repr
