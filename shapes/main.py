import shapes

def create_rectangle():
    ''' 
    Function that prompts user for rectangle length and width,
    calculates the area and perimeter for the rectangle and 
    prints these out (We assume that the lengths and widths will be floats)
    '''
    # Prompts the user for a length and width for the rectangle
    print()
    length = float(input('Rectangle length: '))
    width = float(input('Rectangle width: '))

    # Creates object as an instance of class Rectangle
    rectangle = shapes.Rectangle(length, width)
 
    # Calls the calculate_area function and prints its return value
    print(f'Rectangle area: { rectangle.calculate_area() }')

    # Calls the calculate_perimeter function and prints its return value  
    print(f'Rectangle perimeter: { rectangle.calculate_perimeter() }')
 

def create_circle():
    ''' 
    Function that prompts user for the circle radius,
    calculates the area and circumference for the circle and 
    prints these out (We assume that the input will be a float)
    '''
    # Prompts the user for a radius for the circle
    print()
    radius = float(input('Circle radius: '))

    # Creates object as an instance of class Circle
    circle = shapes.Circle(radius)

    # Calls the calculate_area function and prints its return value
    print(f"Circle area: { circle.calculate_area() }")

    # Calls the calculate_ccircumference function and prints its return value
    print(f"Circle circumference: { circle.calculate_circumference() }")

def show_menu():
    ''' Utility function to show the menu options '''
    print('---\nMenu for shapes program, select an option:')
    print('1 - Create a rectangle.')
    print('2 - Create a circle.')
    print('0 - Stop the program.')
    print('---')
    selection = input('Selection: ')
    if selection == '1' or selection == '2':
        if selection == '1':
            create_rectangle()
            show_menu()
        elif selection == '2':
            create_circle()
            show_menu()

# Mainline of the program
show_menu()