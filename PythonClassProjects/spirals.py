#Kylee Willis
from turtle import Turtle
import random

#does several spirals
def spiral(turtle, size, color, angle=0, count = 0):
    turtle.home() #sets coordinates to (0,0)
    turtle.setheading(angle)
    turtle.color(color[count%len(color)]) #go to the next color in the list - want rainbow, not random
    turtle.pendown()

    for i in range(size):
        turtle.forward(5+i)
        turtle.right(15)

    if count < 11:
        turtle.penup()
        spiral(turtle, size, color, angle+15, count+1)

def main():
    ANIMATION_SPEED = 0
    raphael = Turtle()
    raphael.speed(ANIMATION_SPEED)
    spiral(raphael, 115, ["red", "orange", "yellow", "green", "blue", "purple"])

main()
