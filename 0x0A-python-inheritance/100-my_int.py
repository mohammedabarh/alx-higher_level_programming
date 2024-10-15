#!/usr/bin/python3
"""100-my_int.py
Defines a MyInt class that inherits from int with inverted equality operators.
"""


class MyInt(int):
    """A rebel integer with inverted == and != operators."""

    def __eq__(self, other):
        """Inverts the equality operator."""
        return super().__ne__(other)

    def __ne__(self, other):
        """Inverts the not equal operator."""
        return super().__eq__(other)
