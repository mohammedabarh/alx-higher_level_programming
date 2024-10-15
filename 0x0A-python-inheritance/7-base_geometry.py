#!/usr/bin/python3
"""7-base_geometry.py
Defines a BaseGeometry class with validation methods.
"""


class BaseGeometry:
    """A class representing basic geometric operations."""

    def area(self):
        """Calculates the area of the geometry.

        Raises:
            Exception: If the area method is not implemented.
        """
        raise Exception('area() is not implemented')

    def integer_validator(self, name, value):
        """Validates that value is a positive integer.

        Args:
            name (str): The name of the parameter.
            value (int): The value to validate.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than or equal to 0.
        """
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
