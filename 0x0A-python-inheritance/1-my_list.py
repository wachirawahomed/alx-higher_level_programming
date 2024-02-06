#!/usr/bin/python3
""" MyList module.

Contains class MyList that inherits from list
"""


class MyList(list):
    """
    A class that inherits from list and adds a method to print the list sorted.
    """

    def print_sorted(self):
        """Print the list in ascending order."""
        sorted_list = sorted(self)
        print(sorted_list)
