#!/usr/bin/python3
"""Module containing the text_indentation function."""


def text_indentation(text):
    """Adds two new lines after '.', '?', and ':' characters.

    Args:
        text (str): The input string to be processed.

    Raises:
        TypeError: If the provided text is not of type str.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    for delim in ".?:":
        # Split the text at each delimiter and strip leading spaces
        text = (delim + "\n\n").join(
            [line.strip(" ") for line in text.split(delim)])

    print(text, end="")

if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/5-text_indentation.txt")
