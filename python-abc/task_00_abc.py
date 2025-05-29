#!/usr/bin/python3
"""
ABC classes
"""


from abc import ABC, abstractmethod


class Animal(ABC):
    """
    Abstract class

    Methods
    ----------
    sound:
        the sound the animal makes
    """
    @abstractmethod
    def sound(self):
        pass


class Dog(Animal):
    """
    Subclass of Animal
    """
    def sound(self):
        return ("Bark")


class Cat(Animal):
    """
    Sublass of Animal
    """
    def sound(self):
        return ("Meow")
