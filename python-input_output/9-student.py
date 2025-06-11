#!/usr/bin/python3
"""
This is class Student
"""


class Student:
    """
     A class to represent a student.

    Attributes
    ----------
    first_name:
        student's first name (public)
    last_name:
        student's last name (public)
    age:
        student's age (public)

    Methods
        to_json:
            retrieves a dictionary representation of a Student instance
    -------
    """
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        return (self.__dict__)
