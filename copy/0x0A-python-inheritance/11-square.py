#!/usr/bin/python3
"""11-square.py
Defines a Square class that inherits from Rectangle.
"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Represents a square, inheriting from Rectangle."""

    def __init__(self, size):
        """Initializes a Square instance.

        Args:
            size (int): The size of the square.
        """
        self.integer_validator('size', size)
        self.__size = size
        super().__init__(size, size)  # Call the Rectangle constructor

    def area(self):
        """Calculates the area of the square.

        Returns:
            int: The area of the square (size * size).
        """
        return self.__size * self.__size

    def __str__(self):
        """Returns a string representation of the square.

        Returns:
            str: Informal string representation of the square.
        """
        return f"[Square] {self.__size}/{self.__size}"
