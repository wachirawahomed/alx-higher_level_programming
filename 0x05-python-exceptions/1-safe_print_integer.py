#!/usr/bin/python3
"""Prints an integer"""


def safe_print_integer(value):
    try:
        print("{:d}".format(value))
    except (ValueError, TypeError):
        return False
    return True
