#!/usr/bin/python3
"""

A module with a calss Rectangle.

"""


class Rectangle:
    """
    Defines a rectangle with width and height attributes.
    """

    def __init__(self, width=0, height=0):
        """
        Initializes with specified attributes for the Rectangle object.

        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.

        Raises:
            TypeError: If width or height is not an integer.
            ValueError: If width or height is less than 0.
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """Retrieve the width of the rectangle."""
        return self._width

    @width.setter
    def width(self, value):
        """Set the width of the rectangle."""
        if type(value) is not int:
            raise TypeError('width must be an integer')
        if value < 0:
            raise ValueError('width must be >= 0')
        self._width = value

    @property
    def height(self):
        """Retrieve the height of the rectangle."""
        return self._height

    @height.setter
    def height(self, value):
        """Set the height of the rectangle."""
        if type(value) is not int:
            raise TypeError('height must be an integer')
        if value < 0:
            raise ValueError('height must be >= 0')
        self._height = value
