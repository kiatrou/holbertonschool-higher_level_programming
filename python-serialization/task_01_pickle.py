#!/usr/bin/python3
"""
Serializing and deserializing custom Python objects using
the pickle module
"""


import pickle


class CustomObject:
    """
    A custom class

    Attributes
    ----------
    name(self):
        the name of a student
    age(self):
        the age of a student
    is_student(self):
        true if yes, false if no

    Methods
    ----------
    display(self)
        displays the class attributes
    serialize(self, filename):
        serializes a file
    deserialize(cls, filename):
        deseralizes a file
    """
    def __init__(self, name: str, age: int, is_student: bool):
        if not isinstance(name, str):
            raise TypeError("name must be a string")
        if not isinstance(age, int):
            raise TypeError("age must be an integer")
        if not isinstance(is_student, bool):
            raise TypeError("is_student must be a boolean")

        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Is Student: {self.is_student}")

    def serialize(self, filename):
        # try/except used to handle things like missing files
        # or corrupt data
        try:
            # wb - write binary
            with open(filename, 'wb') as file:
                pickle.dump(self, file)
        except Exception:
            return (None)

    @classmethod
    def deserialize(cls, filename):
        try:
            # rb - read binary
            with open(filename, 'rb') as file:
                object = pickle.load(file)
                return (object)
        except Exception:
            return (None)
