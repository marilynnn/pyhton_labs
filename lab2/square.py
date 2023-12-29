from abc import ABC, abstractmethod
import math


class Figure(ABC):
    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def square(self):
        pass


class Triangle(Figure):

    def __init__(self, side1, side2, side3):
        if not isinstance(side1, (int, float)) or not isinstance(side2, (int, float)) or not isinstance(side3, (int, float)):
            raise TypeError('Sides must be number')
        if side1 <= 0 or side2 <= 0 or side3 <= 0:
            raise ValueError('Sides must be > 0')
        if side1 + side2 <= side3 or side2 + side3 <= side1 or side1 + side3 <= side2:
            raise ValueError('Degenerate triangle')
        self.type = 'Triangle'
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3

    def square(self):
        half_per = (self.side1 + self.side2 + self.side3)/2
        return (half_per * (half_per - self.side1) * (half_per - self.side2) * (half_per - self.side3))**0.5


class Circle(Figure):

    def __init__(self, radius):
        if not isinstance(radius, (int, float)):
            raise TypeError('Radius must be number')
        if radius <= 0:
            raise ValueError('Radius must be > 0')
        self.type = 'Circle'
        self.radius = radius

    def square(self):
        return math.pi * self.radius**2


class Rectangle(Figure):

    def __init__(self, height, width):
        if not isinstance(height, (int, float)) or not isinstance(width, (int, float)):
            raise TypeError('Height and width must be number')
        if height <= 0 and width <= 0:
            raise ValueError('Height and width must be >=0')
        self.type = 'Rectangle'
        self.height = height
        self.width = width

    def square(self):
        return self.height * self.width


a = Triangle(3, 4, 5)
print(a.square())

b = Circle(3)
print(b.square())

c = Rectangle(2, 4)
print(c.square())

print(b.square())

c = Rectangle(2, 4)
print(c.square())
