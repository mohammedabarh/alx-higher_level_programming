#!/usr/bin/python3
"""Defines a class Rectangle."""


class Rectangle:
    """Class for managing the dimensions and representation of a rectangle.

    Attributes:
        number_of_instances (int): Counter of rectangle instances.
        print_symbol (str): Symbol used for the string representation.
    """

    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        """Initializes a new Rectangle instance and increments the instance counter.

        Args:
            width (int): Horizontal dimension of the rectangle. Defaults to 0.
            height (int): Vertical dimension of the rectangle. Defaults to 0.
        """
        type(self).number_of_instances += 1
        self.width = width
        self.height = height

    @property
    def width(self):
        """Gets the width of the rectangle.

        Returns:
            int: The width of the rectangle.
        """
        return self.__width

    @width.setter
    def width(self, value):
        """Sets the width of the rectangle.

        Args:
            value (int): Horizontal dimension of the rectangle.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError('width must be an integer')
        if value < 0:
            raise ValueError('width must be >= 0')
        self.__width = value

    @property
    def height(self):
        """Gets the height of the rectangle.

        Returns:
            int: The height of the rectangle.
        """
        return self.__height

    @height.setter
    def height(self, value):
        """Sets the height of the rectangle.

        Args:
            value (int): Vertical dimension of the rectangle.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError('height must be an integer')
        if value < 0:
            raise ValueError('height must be >= 0')
        self.__height = value

    def area(self):
        """Calculates the area of the rectangle.

        Returns:
            int: The area of the rectangle.
        """
        return self.__width * self.__height

    def perimeter(self):
        """Calculates the perimeter of the rectangle.

        Returns:
            int: The perimeter of the rectangle, or 0 if width or height is 0.
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    def _draw_rectangle(self):
        """Creates a string representation of the rectangle for printing.

        Returns:
            str: Formatted string representing the rectangle.
        """
        rect_str = ""
        for row in range(self.__height):
            rect_str += str(self.print_symbol) * self.__width
            if row < self.__height - 1:
                rect_str += '\n'
        return rect_str

    def __str__(self):
        """Returns a string representation of the rectangle for printing.

        Returns:
            str: The rectangle as a string.
        """
        return self._draw_rectangle()

    def __repr__(self):
        """Returns a string representation of the rectangle for recreation.

        Returns:
            str: The code needed to recreate the rectangle instance.
        """
        return "Rectangle({:d}, {:d})".format(self.__width, self.__height)

    def __del__(self):
        """Handles the deletion of an instance and decrements the instance counter.

        Prints a message when an instance is deleted.
        """
        type(self).number_of_instances -= 1
        print('Bye rectangle...')

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """Compares the area of two rectangles and returns the larger one.

        Args:
            rect_1 (Rectangle): First rectangle to compare.
            rect_2 (Rectangle): Second rectangle to compare.

        Raises:
            TypeError: If either rect_1 or rect_2 is not an instance of Rectangle.

        Returns:
            Rectangle: The rectangle with the larger area, or rect_1 if equal.
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError('rect_1 must be an instance of Rectangle')
        if not isinstance(rect_2, Rectangle):
            raise TypeError('rect_2 must be an instance of Rectangle')
        if rect_1.area() >= rect_2.area():
            return rect_1
        return rect_2
