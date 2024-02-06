#!/usr/bin/python3
"""write_file module.

Contains a function that writes a text file.
"""


def write_file(filename="", text=""):
    """
    Writes a string to a text file (UTF8) and returns the
    number of characters written.

    Args:
        filename (str): The name of the text file.
        text (str): The string to be written to the file.

    Returns:
        int: The number of characters written to the file.
    """
    with open(filename, 'w') as f:
        return f.write(text)
