#!/usr/bin/python3
"""Square module.

This is a module that contain a class that defines
a square and it's init method

"""


class Square:
    """The defination of the square"""

    def __init__(self, size):
        """__init__

        Sets the necessary attributes for the Square object.

        Attributes:
            size (int): The size of the square.

        """
        self.__size = size
