#!/usr/bin/python3
"""This module provides the print_square function."""


def print_square(size):
    """Prints a square made of '#' characters.

    Parameters:
        size: An integer representing the length of the square's side.

    Raises:
        TypeError: If size is not an integer.
        ValueError: If size is less than 0.
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")

    if size < 0:
        raise ValueError("size must be >= 0")

    print(("#" * size + "\n") * size, end="")

if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/4-print_square.txt")
