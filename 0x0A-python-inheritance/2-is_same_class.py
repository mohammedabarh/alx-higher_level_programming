#!/usr/bin/python3
"""Module that defines a function to check object class."""


def is_same_class(obj, a_class):
    """Returns True if the object is exactly an instance of the specified class; otherwise False.

    Args:
        obj: The object to check.
        a_class: The class to compare against.

    Returns:
        bool: True if obj is an instance of a_class, False otherwise.
    """
    return type(obj) is a_class
