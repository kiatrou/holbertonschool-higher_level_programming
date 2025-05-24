#!/usr/bin/python3
"""This module defines an empty Rectangle class."""


class Rectangle:
    """
    A class to represent a rectangle.

    Class Attributes
    ----------
    number_of_instances:
        incremented during each new instance inisialisation
        decremented during each instance deletion
        keeps track of how many rectangles exist

    print_symbol:
        uses "#" symbol for string representation

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
    __repr__(self):
        a string used to look like a Python expression
    __del__(self):
        called when an object is about to be destroyed
    """
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

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
# using [] to create the list
    def __str__(self):
        if self.width == 0 or self.height == 0:
            return ("")
        return "\n".join([str(self.print_symbol) * self.width
                          for _ in range(self.height)])

# __repr__ is a string that looks like a Python expression
    def __repr__(self):
        return (f"Rectangle({self.width}, {self.height})")

    def __del__(self):
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

# this is like a utility tool that belongs in the class but doesn’t
# touch the blueprint or a specific rectangle.
    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return (rect_1)
        else:
            return (rect_2)
