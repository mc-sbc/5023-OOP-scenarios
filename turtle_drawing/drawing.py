class Shape:
    # Initialiser method with 3 attributes
    def __init__(self, colour: str, points, my_turtle):
        self.colour = colour
        self.points = points
        self.my_turtle = my_turtle

    # Draw method for shapes
    def draw_shape(self):
        points = self.points
        self.my_turtle.penup()
        self.my_turtle.goto(points[0].x, points[0].y) # Move to first point in points
        self.my_turtle.color(self.colour)
        self.my_turtle.begin_fill()
        self.my_turtle.pendown()
        # Move to second point in points and iterate to end of list
        for point in points[1:]:
            self.my_turtle.goto(point.x, point.y)
        
        self.my_turtle.end_fill()

class Point:
    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y



    



