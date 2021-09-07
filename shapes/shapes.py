import math

class Rectangle:

    def __init__(self, length: float, width: float):
        self.length = length
        self.width = width
    
    def calculate_area(self):
        return round(self.length * self.width, 2)

    def calculate_perimeter(self):
        return round(2 * self.length + 2 * self.width, 2)

class Circle:

    def __init__(self, radius: float):
        self.radius = radius

    def calculate_area(self):
        return round(math.pi * (self.radius * self.radius), 2)
    
    def calculate_circumference(self):
        return round(math.pi * (self.radius * 2), 2)