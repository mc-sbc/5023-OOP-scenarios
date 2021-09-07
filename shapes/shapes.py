import math

# Create a class called Rectangle
class Rectangle:

    # Initialiser method with 2 attributes and their type hint
    def __init__(self, length: float, width: float):
        self.length = length
        self.width = width
    
    # Function to calculate the area of a rectangle and round result to 2 decimal places
    def calculate_area(self):
        return round(self.length * self.width, 2)

    # Function to calculate the perimeter of a rectangle and round result to 2 decimal places
    def calculate_perimeter(self):
        return round(2 * self.length + 2 * self.width, 2)

# Create a class called Circle
class Circle:

    # Initialiser method with 1 attribute and its type hint
    def __init__(self, radius: float):
        self.radius = radius

    # Function to calculate the area of a circle and round result to 2 decimal places
    def calculate_area(self):
        return round(math.pi * (self.radius * self.radius), 2)
    
    # Function to calculate the circumference of a circle and round result to 2 decimal places
    def calculate_circumference(self):
        return round(math.pi * (self.radius * 2), 2)