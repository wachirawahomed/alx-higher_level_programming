#!/usr/bin/python3
"""append_write module.

Contains a function that appends a text file.
"""


def append_write(filename="", text=""):
    """
    Appends a string at the end of a text file (UTF8) and returns
    the number of characters added.

    Args:
        filename (str): The name of the text file.
        text (str): The string to be appended.

    Returns:
        int: The number of characters added to the file.
    """
    with open(filename, 'a') as f:
        return f.write(text)
