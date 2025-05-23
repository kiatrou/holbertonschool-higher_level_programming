#!/usr/bin/python3
"""This module defines an empty Square class."""


class Square:
    """
    A class to represent a square.

    Attributes
    ----------
    size : int
        size of the square

    Methods
    -------
    area(self):
        Returns the area of a square
    """
    def __init__(self, size=0):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        return (self.__size ** 2)
