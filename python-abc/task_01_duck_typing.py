#!/usr/bin/python3
"""
ABC Class
"""


from abc import ABC, abstractmethod
import math

# Abstract Base Class
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass

# Concrete Class: Circle
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

    def perimeter(self):
        return 2 * math.pi * self.radius

# Concrete Class: Rectangle
class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)

# 🧾 Duck-typed function
def shape_info(shape):
    print("Area:", shape.area())
    print("Perimeter:", shape.perimeter())
