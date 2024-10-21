#!/usr/bin/python3
"""9-rectangle.py
Defines a Rectangle class that inherits from BaseGeometry.
"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Represents a rectangle, inheriting from BaseGeometry."""

    def __init__(self, width, height):
        """Initializes a Rectangle instance.

        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.
        """
        self.integer_validator('width', width)
        self.integer_validator('height', height)
        self.__width = width
        self.__height = height

    def area(self):
        """Calculates the area of the rectangle.

        Returns:
            int: The area of the rectangle (width * height).
        """
        return self.__width * self.__height

    def __str__(self):
        """Returns a string representation of the rectangle.

        Returns:
            str: Informal string representation of the rectangle.
        """
        return f"[Rectangle] {self.__width}/{self.__height}"
