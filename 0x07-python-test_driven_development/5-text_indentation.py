#!/usr/bin/python3
"""
This module contains a function that prints a text with 2 new lines
after each of these characters: ., ? and :
"""


def text_indentation(text):
    """
    Prints a text with 2 new lines after each of these characters: ., ? and :

    Args:
        text (str): The input text.

    Raises:
        TypeError: If text is not a string.
    """
    if type(text) is not str:
        raise TypeError("text must be a string")

    separators = ['.', '?', ':']
    line = ""
    for char in text:
        line += char
        if char in separators:
            print(line.strip())
            print()
            line = ""

    if line.strip():
        print(line.strip())
