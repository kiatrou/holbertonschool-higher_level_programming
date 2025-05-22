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
    size(self):
        Returns value of private attribute __size
    size(self, value):
        Checks to make sure the value is an integer
        Checks to make sure value is greater than 0
    area(self):
        Returns the area of a square
    my_print(self):
        Prints the square according to the size
    """
    def __init__(self, size=0):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        return (self.size ** 2)

    def my_print(self):
        if self.__size == 0:
            print()
        else:
            for i in range(self.__size):
                print("#" * self.__size)
