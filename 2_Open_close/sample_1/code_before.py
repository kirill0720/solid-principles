"""
The AreaCalculator class violates the Open-Closed Principle because it checks
the type of the shape objects in order to calculate their area.

This means that if a new shape class is added in the future,
the AreaCalculator class would need to be modified to include a new conditional statement.
"""


class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height


class AreaCalculator:
    def calculate_area(self, shapes):
        area = 0
        for shape in shapes:
            if isinstance(shape, Rectangle):
                area += shape.width * shape.height
        return area


if __name__ == '__main__':
    shapes = [Rectangle(2, 3), Rectangle(1, 6)]
    calculator = AreaCalculator()
    print(calculator.calculate_area(shapes))
