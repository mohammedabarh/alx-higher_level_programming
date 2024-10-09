#!/usr/bin/python3
"""Module for text_indentation function."""


def text_indentation(text):
    """
    Prints a text with 2 new lines after each of these characters: ., ? and :

    Args:
        text (str): The input text to be formatted.

    Raises:
        TypeError: If text is not a string.
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
            result += '\n\n'
            skip_space = True

    lines = result.split('\n')
    for line in lines:
        print(line.strip())
