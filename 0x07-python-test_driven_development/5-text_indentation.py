#!/usr/bin/python3
"""
This module contains a function that indents text.
"""

def text_indentation(text):
    """
    Prints a text with 2 new lines after each of these characters: ., ? and :

    Args:
        text (str): The input text to be formatted.

    Raises:
        TypeError: If text is not a string.

    Returns:
        None
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    punctuation = ['.', '?', ':']
    result = ""
    skip_space = False

    for char in text:
        if skip_space and char == ' ':
            continue
        
        result += char
        skip_space = False

        if char in punctuation:
            result += "\n\n"
            skip_space = True

    print(result.strip())

if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/5-text_indentation.txt")
