#!/usr/bin/python3
"""
This is a class Rectangle
"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    Class sqaure

    Attributes
    ----------
    size:
        size of a sqaure
    """
    def __init__(self, size):
        self.integer_validator("size", size)
        self.__size = size

    def area(self):
        return (self.__size ** 2)

    def __str__(self):
        return ("[Square] {}/{}".format(self.__width, self.__height))
