#!/usr/bin/python3
"""
add_integer module.

This module contains a function that adds two integers.
"""


def add_integer(a, b=98):
    """Adds two integers.

    Args:
        a (int or float): The first number.
        b (int or float): The second number, default is 98."""

    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    return int(a) + int(b)
