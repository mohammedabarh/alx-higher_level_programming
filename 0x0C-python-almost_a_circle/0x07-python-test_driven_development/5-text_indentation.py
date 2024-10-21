#!/usr/bin/python3
"""
Module for text_indentation function.

This module provides a function to add two new lines
after specific punctuation marks in a given text.
"""


def text_indentation(text):
    """
    Print text with two newlines after '.', '?', and ':'.

    Args:
        text (str): The input text to be formatted.

    Raises:
        TypeError: If text is not a string.
    """
    if type(text) is not str:
        raise TypeError("text must be a string")

    for delim in ".:?":
        text = (delim + "\n\n").join(
            [line.strip(" ") for line in text.split(delim)])

    print("{}".format(text), end="")
