#!/usr/bin/python3
"""2-is_same_class.py: Module to check if an object is of a specific class."""

def is_same_class(obj, a_class):
    """Check if obj is exactly an instance of a_class.

    Args:
        obj: The object to check.
        a_class: The class to compare against.

    Returns:
        True if obj is an instance of a_class; False otherwise.
    """
    return type(obj) == a_class
