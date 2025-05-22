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
    def __init__(self, size=0, position=(0, 0)):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.size = size
        self.position = position

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

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        if not isinstance(value, tuple) or len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value
        if not all(isinstance(num, int) for num in value):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value
        if not all(num >= 0 for num in value):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        return (self.size ** 2)

    def my_print(self):
        if self.size == 0:
            print()
            return
        print("\n" * self.position[1], end="")
        for _ in range(self.size):
            print(" " * self.position[0] + "#" * self.size)
