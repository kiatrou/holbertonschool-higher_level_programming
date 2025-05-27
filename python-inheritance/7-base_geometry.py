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
        public instance - placeholder for area method

    integer_validator(self, name, value):
        Validates that `value` is a positive integer
    """
    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
