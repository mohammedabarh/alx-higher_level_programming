#!/usr/bin/python3
"""Module for the text_indentation function."""


def text_indentation(text):
    """Adds two new lines after each occurrence of '.', '?', or ':'.

    Args:
        text (str): The input string to process.

    Raises:
        TypeError: If the input is not of type str.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    for delim in ".?:":
        # Split the text using the delimiter and strip leading spaces
        text = (delim + "\n\n").join(
            [line.strip(" ") for line in text.split(delim)])

    print(text, end="")

if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/5-text_indentation.txt")
