#!/usr/bin/python3
"""Rectangle class for Holberton Python project 0x08 task 3.
This class defines a rectangle and includes methods for calculating
its area and perimeter, as well as a string representation.
"""

class Rectangle:
    """Represents a rectangle with width and height.

    This class provides methods to calculate the area and perimeter
    of the rectangle.

    Attributes:
        width (int): Horizontal dimension of the rectangle, defaults to 0.
        height (int): Vertical dimension of the rectangle, defaults to 0.

    """

    def __init__(self, width=0, height=0):
        """Initializes the rectangle with given width and height."""
        # Assign width and height using their respective setters
        self.width = width
        self.height = height

    @property
    def width(self):
        """Get the width of the rectangle.

        Returns:
            int: The horizontal dimension of the rectangle.
        """
        return self.__width

    @width.setter
    def width(self, value):
        """Set the width of the rectangle.

        Args:
            value (int): The horizontal dimension of the rectangle.

        Raises:
            TypeError: If `value` is not an integer.
            ValueError: If `value` is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError('width must be an integer')
        if value < 0:
            raise ValueError('width must be >= 0')
        self.__width = value

    @property
    def height(self):
        """Get the height of the rectangle.

        Returns:
            int: The vertical dimension of the rectangle.
        """
        return self.__height

    @height.setter
    def height(self, value):
        """Set the height of the rectangle.

        Args:
            value (int): The vertical dimension of the rectangle.

        Raises:
            TypeError: If `value` is not an integer.
            ValueError: If `value` is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError('height must be an integer')
        if value < 0:
            raise ValueError('height must be >= 0')
        self.__height = value

    def area(self):
        """Calculate the area of the rectangle.

        Returns:
            int: The area of the rectangle (width * height).
        """
        return self.__width * self.__height

    def perimeter(self):
        """Calculate the perimeter of the rectangle.

        Returns:
            int: The perimeter of the rectangle, or 0 if width or height is 0.
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    def _draw_rectangle(self):
        """Create a string representation of the rectangle using '#' characters.

        Returns:
            str: A string suitable for printing the rectangle.
        """
        result = []
        for row in range(self.__height):
            result.append('#' * self.__width)
        return '\n'.join(result)

    def __str__(self):
        """Return a string representation of the rectangle for printing.

        Returns:
            str: The output of _draw_rectangle, representing the rectangle.
        """
        return self._draw_rectangle()
