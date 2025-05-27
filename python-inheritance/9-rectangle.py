#!/usr/bin/python3
"""
This is a class Rectangle
"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    Class rectangle

    Attributes
    ----------
    width:
        private - width of rectangle
    height:
        private - height of rectangle

    Methods
    ----------
    area(self):
        returns the area of a rectangle
    __str__(self):
        defines what gets returned when you use str() or print() on an object
        for this class, return "[Rectangle] {width}/{height}"
    """
    def __init__(self, width, height):
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        return (self.__width * self.__height)

    def __str__(self):
        return ("[Rectangle] {}/{}".format(self.__width, self.__height))
