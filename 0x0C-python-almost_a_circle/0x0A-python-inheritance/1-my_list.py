#!/usr/bin/python3
"""1-my_list.py
A module that defines a MyList class inheriting from the built-in list.
"""


class MyList(list):
    """Class that inherits from list to add a sorting method."""

    def print_sorted(self):
        """Prints the list in ascending order."""
        print(sorted(self))
