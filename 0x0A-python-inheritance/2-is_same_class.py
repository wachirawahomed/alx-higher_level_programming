#!/usr/bin/python3
"""is_same_class module

Contains function that compares an object with an instance.
"""


def is_same_class(obj, a_class):
    """
    Check if the object is exactly an instance of the specified class.

    Args:
        obj (object): The object to check.
        a_class (class): The class to compare with.

    Returns:
        bool: True if the object is an instance of the specified class,
        False otherwise.
    """
    return type(obj) is a_class
