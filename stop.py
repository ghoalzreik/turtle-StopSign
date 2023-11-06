# Ghofran Alzreikat
# Portfolio Project: Turtle - Stop sign
# 11/06/23

import turtle

# Rectangle: takes the width and height as parameters
# and draws a rectangle (each interior angle is 90°)
def rectangle(width, height):
    for i in range(2):
        turtle.pensize(5)
        turtle.forward(height)
        turtle.right(90)
        turtle.forward(width)
        turtle.right(90)

# Octagon: takes the side length as a parameter
# and draws an octagon (each exterior turn is 45°)
def octagon(sidelen):
    for i in range(8):
        turtle.pensize(5)
        turtle.forward(sidelen)
        turtle.left(45)

# Stop: takes the octagon side length as a parameter and draws a stop sign by calling octagon,
# moving forward 3/8 of the side length, and drawing a rectangle sign post that is 1/5 of the side wide
# and has a height that is double a side.
def stop(sidelen):
    octagon(sidelen)
    turtle.forward((3 / 8) * sidelen)
    for i in range(2):
        turtle.forward((1/5) * sidelen)
        turtle.right(90)
        turtle.forward(2*sidelen)
        turtle.right(90)

# Main function to call the Stop function.
def main():
    turtle.speed(0)
    turtle.shape("turtle")
    turtle.color("mediumvioletred")
    turtle.penup()
    turtle.forward(100)
    turtle.pendown()
    stop(90)
    turtle.color("deepskyblue")
    turtle.penup()
    turtle.backward(250)
    turtle.pendown()
    stop(60)

main()
turtle.Screen().exitonclick()
