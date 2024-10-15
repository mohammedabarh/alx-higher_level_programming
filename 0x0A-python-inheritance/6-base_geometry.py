#!/usr/bin/python3

class BaseGeometry:
    """
    A base class for geometry-related operations.
    """

    def area(self):
        """
        Calculate the area of the geometry.

        Raises:
            Exception: Always raises an Exception with the message
                       "area() is not implemented"
        """
        raise Exception("area() is not implemented")
