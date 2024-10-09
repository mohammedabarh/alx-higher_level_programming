#!/usr/bin/python3
"""This module contains the add_integer function."""


def add_integer(a, b=98):
    """Calculate the sum of two integers.

    Parameters:
        a: The first number, expected to be an integer or float.
        b: The second number, expected to be an integer or float, defaults to 98.

    Raises:
        TypeError: If a or b are not of type int or float.

    Returns:
        The total of the two numbers as an integer.
    """

    if type(a) not in (int, float):
        raise TypeError('a must be an integer')
    if type(b) not in (int, float):
        raise TypeError('b must be an integer')
    return int(a) + int(b)

if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/0-add_integer.txt")
