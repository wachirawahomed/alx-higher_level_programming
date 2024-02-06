#!/usr/bin/python3
"""read_file module.

Module for reading a text file and printing its content to stdout.
"""


def read_file(filename=""):
    """
    Reads a text file (UTF8) and prints its content to stdout.

    Args:
        filename (str): The name of the text file to be read.

    Returns:
        None
    """
    with open(filename, 'r') as f:
        print(f.read(), end='')
