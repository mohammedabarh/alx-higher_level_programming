#!/usr/bin/python3
"""101-add_attribute.py
Defines a function to add an attribute to an object if possible.
"""


def add_attribute(obj, attribute, value):
    """Adds a new attribute to an object if possible.

    Args:
        obj: The object to which the attribute is to be added.
        attribute (str): The name of the attribute to add.
        value: The value of the attribute.

    Raises:
        TypeError: If the object can't have new attributes.
    """
    if not hasattr(obj, '__dict__'):
        raise TypeError("can't add new attribute")

    setattr(obj, attribute, value)
