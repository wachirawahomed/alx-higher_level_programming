#!/usr/bin/python3
"""Square module.

This module defines a Square class representing a square with a specific size.

"""


class Square():
    """The defination of the square

    Attributes:
        size (int): The size of one edge of the square.

    """

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
        """Gets the current size of the square.

        Returns:
            int: The size of one edge of the square.
        """
        return self.__size

    @size.setter
    def size(self, size):
        """Sets the size of the square.

        Args:
            size (int): The size of one edge of the square.

         Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        """
        if type(size) is not int:
            raise TypeError('size must be an integer')

        if size < 0:
            raise ValueError('size must be >= 0')

        self.__size = size

    def area(self):
        """Calculates the area of the square.

        Returns:
            int: The area of the square.
        """
        return self.__size ** 2
