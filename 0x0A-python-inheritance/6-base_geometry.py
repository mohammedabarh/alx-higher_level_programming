#!/usr/bin/python3
"""Module for geometric operations."""

class BaseGeometry:
    """A class to represent basic geometric shapes."""

    def area(self):
        """Calculate the area of the shape.

        Raises:
            Exception: If the area method is not implemented in a derived class.
        """
        raise Exception('area() is not implemented')
