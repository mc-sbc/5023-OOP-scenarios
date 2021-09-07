import turtle
import drawing

# A list of shapes, which we'll loop through later in the program to draw our shapes
shapes = []

# Creates an instance of a turtle which will be used for drawing the shapes
my_turtle = turtle.Turtle()

# Create a list of Point objects then a Shape object
bt_points = [
    drawing.Point(-120, 200),
    drawing.Point(-20, 200),
    drawing.Point(-70, 100)
    ]
bt = drawing.Shape('blue', bt_points, my_turtle)
# Adds the blue triangle to the list of shapes
shapes.append(bt)

# Create a list of Point objects then a Shape object
os_points = [
    drawing.Point(-200, -100),
    drawing.Point(-200, -150),
    drawing.Point(-150, -150),
    drawing.Point(-150, -100)
    ]
os = drawing.Shape('orange', os_points, my_turtle)
# Adds the orange square to the list of shapes
shapes.append(os)

# Create a list of Point objects then a Shape object
rt_points = [ drawing.Point(100, 200), drawing.Point(250, 200), drawing.Point(175, 50) ]
rt = drawing.Shape('red', rt_points, my_turtle)
# Adds the red triangle to the list of shapes
shapes.append(rt)

# Create a list of Point objects then a Shape object
gh_points = [ 
    drawing.Point(120, -120),
    drawing.Point(156, -120),
    drawing.Point(174, -151),
    drawing.Point(156, -182),
    drawing.Point(120, -182),
    drawing.Point(102, -151),
    ]
gh = drawing.Shape('green', gh_points, my_turtle)
# Adds the green hexagon to the list of shapes
shapes.append(gh)

# Draws all of the shapes that are in the shapes list in the window
for shape in shapes:
    shape.draw_shape()

# Hide turtle
my_turtle.hideturtle()

# This line will mean that the Turtle window won't close until we click
turtle.Screen().exitonclick() 