#!/usr/bin/python3
"""
This module defines a function to read a text file
and print its content to standard output.
"""


def read_file(filename=""):
    """Read a text file (UTF8) and print its content to stdout.

    Args:
        filename (str): The name of the file to read. Defaults to an empty string.
    """
    with open(filename, 'r', encoding='utf-8') as file:
        print(file.read(), end="")
