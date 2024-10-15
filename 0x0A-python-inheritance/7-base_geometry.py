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

    def integer_validator(self, name, value):
        """
        Validate that a value is a positive integer.

        Args:
            name (str): The name of the value being validated.
            value: The value to validate.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than or equal to 0.
        """
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
