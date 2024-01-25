#!/usr/bin/python3
"""Square module.

This is a class that defines a square and it's init method

"""


class Square():
    """The defination of the square"""

    def __init__(self, size=0):
        """__init__
        Sets the necessary attributes for the Square object.

        Attributes:
            size (int): the size of one edge of the square.

        Raises:
            TypeError: If `size` type is not `int`.
            ValueError: If `size` is less than `0`.

        """

        if type(size) is not int:
            raise TypeError('size must be an integer')

        if size < 0:
            raise ValueError('size must be >= 0')

        self.__size = size
