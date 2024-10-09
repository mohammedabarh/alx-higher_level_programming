#!/usr/bin/python3
"""This module contains the say_my_name function."""


def say_my_name(first_name, last_name=""):
    """Prints the full name.

    Parameters:
        first_name: A string representing the first name.
        last_name: A string representing the last name.

    Raises:
        TypeError: If first_name or last_name is not a string.
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")

    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")

    print("My name is {:s} {:s}".format(first_name, last_name))

if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/3-say_my_name.txt")
