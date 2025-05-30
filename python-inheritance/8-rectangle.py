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
    """
    def __init__(self, width, height):
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
