#!/usr/bin/python3
"""Module that defines a Square class with a private size attribute."""


class Square:
    """A class that represents a square with a private size attribute."""

    def __init__(self, size):
        """Initialize the square with a given size.

        Args:
            size (int): The size of the square.
        """
        self.__size = size  # Private instance attribute
