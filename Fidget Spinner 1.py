from turtle import *

# Presets before code really runs
hideturtle()
width(5)
speed(2)  # Set the drawing speed (adjust as needed)
total_rotation = 0

# Functions
def reset():
    penup()
    goto(0, 0)
    pendown()

def move_whole_drawing():
    global total_rotation
    total_rotation += 25

    try:
        if window_exists():  # Check if the window is still open
            clear()
            setheading(total_rotation)
            draw_fidget_spinner()
            ontimer(move_whole_drawing, 50)  # Repeat every 50 milliseconds
    except Terminator:
        pass  # Handle Terminator directly

def draw_fidget_spinner():
    try:
        penup()  # Lift the pen
        reset()
        pencolor("black")  # Set the pen color to black

        # Draw the blue line
        pendown()
        forward(100)
        pencolor("blue")
        dot(50)
        penup()

        # Reset position to the center
        reset()

        # Draw the green line
        setheading(120 + total_rotation)  # Set the direction to 120 degrees (counter-clockwise)
        pendown()
        pencolor("black")  # Set the pen color to black
        forward(100)
        pencolor("green")
        dot(50)
        penup()

        # Reset position to the center
        reset()

        # Draw the red line
        setheading(-120 + total_rotation)  # Set the direction to -120 degrees (clockwise)
        pendown()
        pencolor("black")  # Set the pen color to black
        forward(100)
        pencolor("red")
        dot(50)
        penup()

        # Reset position to the centre
        reset()
    except Terminator:
        pass  # Handle Terminator directly

def window_exists():
    try:
        # Try to access some property of the turtle Screen
        Screen().window_width()
        return True
    except Terminator:
        return False

# Set starting point
reset()

# Draw the fidget spinner initially
draw_fidget_spinner()

# Call move_whole_drawing to start the animation
move_whole_drawing()

# Listen for key events
listen()

# Keep the window open
mainloop()



""" buggy with animations
from turtle import *

# Presets before code really runs
hideturtle()
width(5)
speed(2)  # Set the drawing speed (adjust as needed)
total_rotation = 0

# Functions
def reset():
    penup()
    goto(0, 0)
    pendown()

def move_whole_drawing():
    global total_rotation
    total_rotation += 25

    if window_exists():  # Check if the window is still open
        clear()
        setheading(total_rotation)
        draw_fidget_spinner()
        ontimer(move_whole_drawing, 50)  # Repeat every 50 milliseconds

def draw_fidget_spinner():
    penup()  # Lift the pen
    reset()
    pencolor("black")  # Set the pen color to black

    # Draw the blue line
    pendown()
    forward(100)
    pencolor("blue")
    dot(50)
    penup()

    # Reset position to the center
    reset()

    # Draw the green line
    setheading(120 + total_rotation)  # Set the direction to 120 degrees (counter-clockwise)
    pendown()
    pencolor("black")  # Set the pen color to black
    forward(100)
    pencolor("green")
    dot(50)
    penup()

    # Reset position to the center
    reset()

    # Draw the red line
    setheading(-120 + total_rotation)  # Set the direction to -120 degrees (clockwise)
    pendown()
    pencolor("black")  # Set the pen color to black
    forward(100)
    pencolor("red")
    dot(50)
    penup()

    # Reset position to the centre
    reset()

def window_exists():
    try:
        # Try to access some property of the turtle Screen
        Screen().window_width()
        return True
    except turtle.Terminator:
        return False

# Set starting point
reset()

# Draw the fidget spinner initially
draw_fidget_spinner()

# Call move_whole_drawing to start the animation
move_whole_drawing()

# Listen for key events
listen()

# Keep the window open
mainloop()
"""



""" Working without animation
from turtle import *

# Presets before code really runs
hideturtle()
width(5)
speed(200)
total_rotation = 0

# Functions
def reset():
    penup()
    goto(0, 0)
    pencolor("black")
    pendown()

def move_whole_drawing():
    global speed
    global total_rotation
    total_rotation += 25
    clear()
    setheading(total_rotation)
    draw_fidget_spinner()

def draw_fidget_spinner():
    # Draw the blue line
    forward(100)
    pencolor("blue")
    dot(50)

    # Reset position to the center
    reset()

    # Draw the green line
    setheading(120 + total_rotation)  # Set the direction to 120 degrees (counter-clockwise)
    forward(100)
    pencolor("green")
    dot(50)

    # Reset position to the center
    reset()

    # Draw the red line
    setheading(-120 + total_rotation)  # Set the direction to -120 degrees (clockwise)
    forward(100)
    pencolor("red")
    dot(50)

    # Reset position to the centre
    reset()

# Set starting point
reset()

# Draw the fidget spinner initially
draw_fidget_spinner()

# Bind the function to the space key
onkey(move_whole_drawing, 'space')

# Listen for key events
listen()

# Close the drawing window when clicked
exitonclick()
"""
