#!/usr/bin/python3
"""Defines a Rectangle class."""


class Rect:
    """
    A class representing a rectangle with specified dimensions.

    Attributes:
        width (int): The width of the rectangle.
        height (int): The height of the rectangle.
    """

    def __init__(self, width=0, height=0):
        """Initializes a new Rect instance.

        Args:
            width (int, optional): The width of the rectangle. Defaults to 0.
            height (int, optional): The height of the rectangle. Defaults to 0.
        """
        self.height = height
        self.width = width

    @property
    def width(self):
        """Gets the width of the rectangle.

        Returns:
            int: The width value.
        """
        return self.__width

    @property
    def height(self):
        """Gets the height of the rectangle.

        Returns:
            int: The height value.
        """
        return self.__height

    @width.setter
    def width(self, value):
        """Sets the width of the rectangle.

        Args:
            value (int): The new width.

        Raises:
            TypeError: If the value is not an integer.
            ValueError: If the value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("Width must be an integer")
        if value < 0:
            raise ValueError("Width must be >= 0")
        self.__width = value

    @height.setter
    def height(self, value):
        """Sets the height of the rectangle.

        Args:
            value (int): The new height.

        Raises:
            TypeError: If the value is not an integer.
            ValueError: If the value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("Height must be an integer")
        if value < 0:
            raise ValueError("Height must be >= 0")
        self.__height = value

    def area(self):
        """Calculates the area of the rectangle.

        Returns:
            int: The area of the rectangle.
        """
        return self.__height * self.__width

    def perimeter(self):
        """Calculates the perimeter of the rectangle.

        Returns:
            int: The perimeter of the rectangle.
        """
        if self.__height == 0 or self.__width == 0:
            return 0
        return 2 * (self.__height + self.__width)

    def __str__(self):
        """Returns a string representation of the rectangle using '#' characters.

        Returns:
            str: A string depicting the rectangle.
        """
        if self.__width == 0 or self.__height == 0:
            return ""

        return "\n".join(["#" * self.__width for _ in range(self.__height)])
