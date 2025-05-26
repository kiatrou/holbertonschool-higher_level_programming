#!/usr/bin/python3
"""
This is a class BaseGeometry
"""


class BaseGeometry:
    """
    This is a BaseGeometry class

    Method
    ----------
    area(self):
        public instance - raises an exception "area() is not implemented"
    """
    def area(self):
        raise Exception("area() is not implemented")
