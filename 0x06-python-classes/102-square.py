#!/usr/bin/python3
"""Square module.

This module defines a Square class representing a square with a specific size.

"""


class Square:
    """The defination of the square

    Args:
     size (int): the size of one edge of the square.

    """

    def __init__(self, size=0):
        """__init__

        Initializes the size value and position of the square.

        Args:
            size (int): the size of one edge of the square.

        Raises:
            TypeError: If `size` type is not `int`.
            ValueError: If `size` is less than `0`.

        """
        self.size = size

    def __eq__(self, other):
        """Sets the compare equality behavior of the Square object.

        Args:
            other (Square): the Square object to compare with.
        """
        if type(other) is Square:
            return self.area() == other.area()

    def __lt__(self, other):
        """Sets the compare less than behavior of the Square object.

        Args:
            other (Square): the Square object to compare with.
        """
        if type(other) is Square:
            return self.area() < other.area()

    def __le__(self, other):
        """Sets the compare less equal than behavior of the Square object.

        Args:
            other (Square): the Square object to compare with.
        """
        if type(other) is Square:
            return self.area() <= other.area()

    @property
    def size(self):
        """Gets the current size of the square.

        Returns:
            int: The size of the square.

        """
        return self.__size

    @size.setter
    def size(self, size):
        """size setter method.

        Sets the size of the square.

        Args:
            size (int): The new size of the square.

        Raises:
            TypeError: If `size` type is not `int`.
            ValueError: If `size` is less than `0`.

        """
        if type(size) is not int:
            raise TypeError('size must be an integer')

        if size < 0:
            raise ValueError('size must be >= 0')

        self.__size = size

    def area(self):
        """Returns the current square area."""
        return self.__size ** 2
