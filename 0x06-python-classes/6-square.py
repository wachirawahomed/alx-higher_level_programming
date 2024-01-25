#!/usr/bin/python3
class Square:
    """Square Class

    A Square Class

    """

    def __init__(self, size=0, position=(0, 0)):
        """__init__

        Initializes the size value and position of the square.

        Args:
            size (int): the size of one edge of the square.
            position (tuple): The position of the square.

        Raises:
            TypeError: If `size` type is not `int`.
            ValueError: If `size` is less than `0`.
            TypeError: If `position` is not a tuple of 2 positive integers.

        """
        self.size = size
        self.position = position

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

    @property
    def position(self):
        """Gets the current position of the square.

        Returns:
            tuple: The position of the square.

        """
        return self.__position

    @position.setter
    def position(self, position):
        """position setter method.

        Sets the position of the square.

        Args:
            position (tuple): The new position of the square.

        Raises:
            TypeError: If `position` is not a tuple of 2 positive integers.

        """
        if not self.__check_position(position):
            raise TypeError('position must be a tuple of 2 positive integers')

        self.__position = position

    def __check_position(self, position):
        """Check if position is a tuple of 2 positive integers.

        Args:
            position (tuple): The position to check.

        Returns:
            bool: True if position is valid, False otherwise.

        """
        return (
            self.__check_tuple(position) and
            self.__check_indexes(position) and
            self.__check_integers(position) and
            self.__check_values(position)
        )

    def __check_tuple(self, position):
        """Check if position is a tuple.

        Args:
            position (tuple): The position to check.

        Returns:
            bool: True if position is a tuple, False otherwise.

        """
        return type(position) is tuple

    def __check_indexes(self, position):
        """Check if position has two elements.

        Args:
            position (tuple): The position to check.

        Returns:
            bool: True if position has two elements, False otherwise.

        """
        return len(position) == 2

    def __check_integers(self, position):
        """Check if elements of position are integers.

        Args:
            position (tuple): The position to check.

        Returns:
            bool: True if elements of position are integers, False otherwise.

        """
        return type(position[0]) is int and type(position[1]) is int

    def __check_values(self, position):
        """Check if elements of position are positive.

        Args:
            position (tuple): The position to check.

        Returns:
            bool: True if elements of position are positive, False otherwise.

        """
        return position[0] >= 0 and position[1] >= 0

    def area(self):
        """Returns the current square area.

        Returns:
            int: The area of the square.

        """
        return self.__size ** 2

    def my_print(self):
        """Prints the square with the # character on stdout."""
        if self.__size == 0:
            print()
            return None

        for _ in range(self.__position[1]):
            print()

        for i in range(1, self.area() + 1):
            if i % self.__size == 1:
                print(' ' * self.__position[0], end='')
                print('#', end='')
            else:
                print('#', end='')

            if i % self.__size == 0 and i > 0:
                print()
