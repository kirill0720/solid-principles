"""
The solution is to create an abstract Shape class that defines the area() method as abstract.
The Rectangle, Circle and any other classes then inherit from the Shape class and implement the area() method.

This way, the AreaCalculator class can simply call the area() method on each shape object
without needing to know its specific type.
"""

from abc import ABC, abstractmethod


class Shape(ABC):
    @abstractmethod
    def area(self):
        pass


class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2


class AreaCalculator:
    def calculate_area(self, shapes):
        area = 0
        for shape in shapes:
            if isinstance(shape, Shape):
                area += shape.area()
        return area


if __name__ == '__main__':
    shapes = [Rectangle(2, 3), Circle(2), Rectangle(1, 6), Circle(3)]
    calculator = AreaCalculator()
    print(calculator.calculate_area(shapes))
