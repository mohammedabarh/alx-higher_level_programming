#!/usr/bin/python3
"""Module that defines a Square class with size validation and area calculation."""


class Square:
    """A class that represents a square with a private size attribute."""

    def __init__(self, size=0):
        """Initialize the square with a given size.

        Args:
            size (int, optional): The size of the square. Defaults to 0.

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size  # Private instance attribute

    def area(self):
        """Calculate the area of the square.

        Returns:
            int: The area of the square.
        """
        return self.__size ** 2  # Area calculation
