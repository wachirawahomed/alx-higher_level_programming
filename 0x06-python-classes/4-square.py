#!/usr/bin/python3
"""Square module.

This is a class that defines a square and it's init method

"""


class Square():
    """The defination of the square"""

    def __init__(self, size=0):
        """__init__
        Initializes the size of the Square.

        Attributes:
            size (int): the size of one edge of the square.

        Raises:
            TypeError: If size type is not given as int.
            ValueError: if size is less than 0
        """

        self.__size = size

        @property
        def size(self):
            """Gets the current square area"""
            return self.__size

        @size.setter
        def size(self, size):
            if type(size) is not int:
                raise TypeError('size must be an integer')

            if size < 0:
                raise ValueError('size must be >= 0')

            self.__size = size

        def area(self):
            """Returns the current square area"""
            return self.__size ** 2
