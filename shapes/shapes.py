from shapes.main import create_circle


class Rectangle:

    def __init__(self, length: float, width: float):
        self.length = length
        self.width = width
    
    def calculate_area(self):
        return round(self.length * self.width, 2)

    def calculate_perimemter(self):
        return round(2 * self.length + 2 * self.width, 2)

