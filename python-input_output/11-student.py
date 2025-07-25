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
            If attrs is a list of strings, only attributes name contain in this
            list must be retrieved.
            Otherwise, all attributes must be retrieved

        reload_from_json:
            replaces all attributes of the Student instance
    -------
    """
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        if isinstance(attrs, list):
            new_dictionary = {}
            for i in attrs:
                # If attrs is not a list (or is None), return all attributes
                if i in self.__dict__:
                    # add it to new_dictionary
                    new_dictionary[i] = self.__dict__[i]
            return (new_dictionary)
    # If attrs is not a list (or is None), return all attributes
        else:
            return (self.__dict__)

    def reload_from_json(self, json):
        # loops over all key:value pairs in the json dictionary
        for key, value in json.items():
            # sets an attribute named key on the object self to the value value
            setattr(self, key, value)
            # This method updates the object’s attributes using the
            # key-value pairs provided.
            # It replaces existing attributes or adds new ones dynamically
            # based on the dictionary.
