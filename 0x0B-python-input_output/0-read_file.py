#!/usr/bin/python3
"""read_file module.

Contains a function that reads a text file.
"""


def read_file(filename=""):
    """
    Appends a string at the end of a text file (UTF8) and returns
    the number of characters added.

    Args:
        filename (str): The name of the text file.
        text (str): The string to be appended.

    Returns:
        int: The number of characters added to the file.
    """
    with open(filename, 'r') as f:
        print(f.read(), end='')
