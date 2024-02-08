#!/usr/bin/python3
"""add_attribute module.

Contains function that checks.
"""

def add_attribute(obj, attr_name, attr_value):
    """
    Adds a new attribute to an object if possible, otherwise raises a TypeError.

    Args:
        obj: The object to which the attribute will be added.
        attr_name: The name of the attribute to be added.
        attr_value: The value of the attribute to be added.

    Raises:
        TypeError: If the object cannot have new attributes.
    """
    if not hasattr(obj, '__dict__'):
        raise TypeError("can't add new attribute")
    setattr(obj, name, value)
