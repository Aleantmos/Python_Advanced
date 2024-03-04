import math


class Circle:
    def __init__(self, radius):
        self._radius = radius
        self._pi = 3.14

    def set_radius(self, new_radius):
        self._radius = new_radius

    def get_area(self):
        return self._pi * math.pow(self._radius, 2)

    def get_circumference(self):
        return 2 * self._pi * self._radius


circle = Circle(10)
circle.set_radius(12)
print(circle.get_area())
print(circle.get_circumference())

