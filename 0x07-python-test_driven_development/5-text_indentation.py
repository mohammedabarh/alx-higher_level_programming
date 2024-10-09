#!/usr/bin/python3
"""This module provides the text_indentation function."""


def text_indentation(text):
    """Adds two new lines after each occurrence of '.', '?', or ':'.

    Parameters:
        text: A string to be processed.

    Raises:
        TypeError: If the input is not a string.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    for delimiter in ".?:":  # Iterate through the specified delimiters
        text = (delimiter + "\n\n").join(
            [line.strip(" ") for line in text.split(delimiter)]
        )

    print(text, end="")

if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/5-text_indentation.txt")
