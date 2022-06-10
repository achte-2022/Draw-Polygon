#Importing Libraries
from turtle import Turtle, Screen
import random

#Constants
SIDE_LENGTH = 75
MAX_INTENSITY = 255
WIDTH = 5

def draw_polygon(turtle_object, num_sides, side_length):
    angle = 360 / num_sides
    for _ in range(num_sides):
        turtle_object.forward(side_length)
        turtle_object.right(angle)
    return

#Object Setup
window = Screen()
turtle_object = Turtle()
turtle_object.width(WIDTH)

#Color Setup
window.colormode(MAX_INTENSITY)

for i in range(3, 11):
    red = random.randint(0, MAX_INTENSITY)
    green = random.randint(0, MAX_INTENSITY)
    blue = random.randint(0, MAX_INTENSITY)
    turtle_object.color((red, green, blue))
    draw_polygon(turtle_object, i, side_length=SIDE_LENGTH)

turtle_object.hideturtle()
window.exitonclick()
