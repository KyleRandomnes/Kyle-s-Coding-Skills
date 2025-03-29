from turtle import *
import random

#global vars
Angle = 0
total_height = 0
my_angles_list = [45, 55, 65, 75, 85, 95, 105, 115, 125]
my_colors_list = [
    "orange", "yellow", "green", "blue", "purple",
    "pink", "cyan", "magenta", "violet", "indigo", "darkred",
    "darkorange", "darkgreen", "darkblue", "darkviolet", "darkcyan",
    "darkmagenta"
]


#heart made
hideturtle()
color("red")
begin_fill()
pensize(3)
left(50)
forward(150)
circle(57, 200)
right(140)
circle(57, 200)
forward(150)
end_fill()

#Functions
def reset():
    penup()
    goto(0, 0)
    setheading(90)
    pendown()
    color("green")

def VineDistance():
    global total_height
    if total_height<80:
        num = random.randint(3, 15)
        total_height += num
        return num
    elif total_height < 120:
        num = random.randint(5, 10)
        total_height += num
        return num
    else:
        return 0

def VineLeftAngle():
    global Angle
    if 125 > Angle:
        return random.randint(15, 25)
    elif Angle > 50:
        return random.randint(-25, -15)
    return 0

def VineRightAngle():
    global Angle
    if Angle > 50:
        return random.randint(15, 25)
    elif 125 > Angle:
        return random.randint(-25, -15)
    return 0

def FlowerPaint():
    global my_colors_list
    placement = 0
    count = random.randint(3, 8)
    random_choice = random.choice(my_colors_list)
    my_colors_list.remove(random_choice)
    color(random_choice)
    header = 360/count
    #drawing petals
    while count > 0:
        placement = placement + header
        setheading(placement)
        begin_fill()
        circle(15, 90)
        right(270)
        circle(15, 90)
        end_fill()
        count -= 1
    #drawing dot
    random_choice = random.choice(my_colors_list)
    my_colors_list.remove(random_choice)
    dot(10, random_choice)
    reset()

    
def VinesPaint():
    global Angle
    global total_height
    total_height = 0
    for _ in range(random.randint(15, 25)):
        Angle = heading()
        num = random.randint(1, 10)
        if(num < 6):
            left(VineLeftAngle())
        else:
            right(VineRightAngle())
        forward(VineDistance())
    FlowerPaint()


#reset
reset()

#roots
color("green")
for _ in range(5):
    random_choice = random.choice(my_angles_list)
    setheading(random_choice)
    my_angles_list.remove(random_choice)
    forward(20)
    VinesPaint()

#Finished
done()

