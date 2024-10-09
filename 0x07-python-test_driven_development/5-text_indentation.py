#!/usr/bin/python3
"""Module for text_indentation method."""


def text_indentation(text):
    """
    Print text with 2 new lines after each '.', '?', and ':'.

    Args:
        text (str): The text to print.

    Raises:
        TypeError: If text is not a string.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    punctuation = ['.', '?', ':']
    current_line = ""

    for char in text:
        current_line += char
        if char in punctuation:
            print(current_line.strip())
            print()
            current_line = ""

    if current_line:
        print(current_line.strip(), end="")
