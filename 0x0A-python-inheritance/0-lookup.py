#!/usr/bin/python3
"""Lookup module.

Contains a function that returns the list of
available attributes and methods of an object
"""


def lookup(obj):
    """
    Return the list of available attributes and methods of an object.

    Args:
        obj (object): The object for which to retrieve attributes and methods.

    Returns:
        list: A list containing the names of all attributes and methods.
    """
    return dir(obj)
