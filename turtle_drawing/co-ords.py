''' 
    Program used to print out co-ordinates for different shapes.
    This one is set to draw a hexagon
'''

import turtle

sides = int(input('Sides: '))
length = int(input('Length: '))
start_x = int(input('x co-ord: '))
start_y = int(input('y co-ord: '))

turtle.penup() 
turtle.goto(start_x, start_y) # starting position
turtle.pendown()
              
print(round(turtle.xcor()), round(turtle.ycor()))

#executing loop 6 times for 6 sides 
for i in range(sides): 
    
  #Move forward by 90 units  
  turtle.forward(36) 
    
  #Turn left the turtle by 300 degrees 
  turtle.left(360-(360/sides))

  print(round(turtle.xcor()), round(turtle.ycor()))