import turtle
from PIL import Image

# Function to convert an image to a binary representation
def image_to_binary(image_path, threshold=128):
    image = Image.open(image_path).convert("L")
    binary_image = image.point(lambda p: p > threshold and 255)
    return binary_image

# Function to trace the outline of a binary image using Turtle
def trace_image(binary_image):
    turtle.speed(2)
    turtle.shape("turtle")

    width, height = binary_image.size

    for y in range(-height // 2, height // 2):
        turtle.penup()
        turtle.goto(-width // 2, y)
        turtle.pendown()

        for x in range(-width // 2, width // 2):
            pixel_color = binary_image.getpixel((x + width // 2, y + height // 2))
            if pixel_color == 0:  # If the pixel is black, move the turtle
                turtle.forward(1)
            else:
                turtle.penup()
                turtle.forward(1)
                turtle.pendown()

# Specify the path to the image
image_path = "C:\Users\kylej\OneDrive\Pictures\Slide Shows"

# Set the threshold for converting the image to binary
threshold_value = 128

# Convert the image to binary
binary_image = image_to_binary(image_path, threshold_value)

# Trace the outline of the binary image using Turtle
trace_image(binary_image)

# Keep the window open until the user closes it
turtle.mainloop()
