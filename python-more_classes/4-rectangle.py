#!/usr/bin/python3
"""This module defines an empty Rectangle class."""


class Rectangle:
    """
    A class to represent a rectangle.

    Attributes
    ----------
    width(self):
        Returns value of private attribute __width
    height(self):
        Returns value of private attribute __height

    Methods
    -------
    area(self):
        returns the area of a rectangle
    perimeter(self):
        returns the rectangle perimeter
    __str__(self):
        prints the rectangle using #
    """
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        return (self.width * self.height)

    def perimeter(self):
        if self.width == 0 or self.height == 0:
            return (0)
        return ((self.width + self.height) * 2)

# used to define the "informal" or human-readable string representation
# of an object
    def __str__(self):
        if self.width == 0 or self.height == 0:
            return ("")
        shape = []
        for i in range(self.height):
            shape.append("#" * self.width)
        return ("\n".join(shape))

# __repr__ is a string that looks like a Python expression
    def __repr__(self):
        return (f"Rectangle({self.width}, {self.height})")
