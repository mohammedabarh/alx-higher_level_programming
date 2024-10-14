#!/usr/bin/python3
"""1-my_list.py
A module that defines a MyList class inheriting from the built-in list.
"""


class MyList(list):
    """A class that extends the built-in list type."""

    def print_sorted(self):
        """Prints the list in ascending order."""
        print(sorted(self))
