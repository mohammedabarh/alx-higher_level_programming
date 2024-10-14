#!/usr/bin/python3
def lookup(obj):
    """Returns a list of attributes and methods of the given object.

    Args:
        obj: The object to inspect.

    Returns:
        A list of attributes and methods of the object.
    """
    return dir(obj)
