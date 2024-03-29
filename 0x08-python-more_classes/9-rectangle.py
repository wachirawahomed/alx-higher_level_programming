#!/usr/bin/python3
"""
A module with a class Rectangle
"""


class Rectangle:
    """
    Defines a rectangle with width and height attributes.
    """

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """
        Initializes a rectangle with specified width and height.

        Args:
            width (int, optional): The width of the rectangle.
            height (int, optional): The height of the rectangle.

        Raises:
            TypeError: If width or height is not an integer.
            ValueError: If width or height is less than 0.
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """
        Retrieve the width of the rectangle.
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Set the width of the rectangle.

        Args:
            value (int): The width of the rectangle.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than 0.
        """
        if type(value) is not int:
            raise TypeError('width must be an integer')
        if value < 0:
            raise ValueError('width must be >= 0')
        self.__width = value

    @property
    def height(self):
        """
        Retrieve the height of the rectangle.
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Set the height of the rectangle.

        Args:
            value (int): The height of the rectangle.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than 0.
        """
        if type(value) is not int:
            raise TypeError('height must be an integer')
        if value < 0:
            raise ValueError('height must be >= 0')
        self.__height = value

    def area(self):
        """
        Calculate the area of the rectangle.

        Returns:
            int: The area of the rectangle.
        """
        return self.__width * self.__height

    def perimeter(self):
        """
        Calculate the perimeter of the rectangle.

        Returns:
            int: The perimeter of the rectangle.
        """
        if self.__width != 0 and self.__height != 0:
            return 2 * (self.__width + self.__height)
        return 0

    def __str__(self):
        """
        Return a string representation of the rectangle.

        Returns:
            str: A string representation of the rectangle.
        """
        result = ""
        if self.__width == 0 or self.__height == 0:
            return result

        for _ in range(self.__height):
            result += str(self.print_symbol) * self.__width + "\n"

        return result[:-1]

    def __repr__(self):
        """
        Return a string representation of the rectangle
        that can be used to recreate the instance.

        Returns:
            str: A string representation of the rectangle.
        """
        return f"Rectangle({self.__width}, {self.__height})"

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """

        Compares the biggest or equal area value between two Rectangles

        Args:
            rect_1 (Rectangle): The first Rectangle to compare
            rect_2 (Rectangle): The second Rectangle to compare

        Returns:
            Rectangle: The biggest Rectangle, or `rect_1` if the
            two Rectangles have the same area value.

        Raises:
            TypeError: If `rect_1` or `rect_2` aren't an instance
            of the Rectangle class.

        """
        if type(rect_1) is not Rectangle:
            raise TypeError("rect_1 must be an instance of Rectangle")
        if type(rect_2) is not Rectangle:
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_2.area() > rect_1.area():
            return rect_2
        return rect_1

    @classmethod
    def square(cls, size=0):
        """Returns a new Rectangle instance with equal width and height"""
        return cls(size, size)

    def __del__(self):
        """
        Print a message when an instance of Rectangle is deleted.
        """
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 2
