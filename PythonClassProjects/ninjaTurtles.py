#Kylee Willis
from turtle import *
import time

#I promise this technically uses recursion :)

def ninja(turtle, color, x, y): #essentially calls other functions
    RADIUS = 40
    face(turtle, 0, x, y, RADIUS)
    mask(turtle, 0, x+RADIUS, y+RADIUS, color, RADIUS, 150)
    turtle.hideturtle()

#draw the green face background
def face(turtle, count, x, y, radius):
    turtle.penup()
    turtle.setx(x)
    turtle.sety(y)
    turtle.pendown()
    
    turtle.color("green", "green")
    turtle.begin_fill()
    turtle.circle(radius)
    turtle.end_fill()

    if count < 3:
        if count == 0:
            y -= 25
        if count == 1:
            x -= 25
            y += 8
            radius -= 5
        if count == 2:
            x += 50
            face(turtle, count+1, x, y, radius)
        else:
            face(turtle, count + 1, x, y, radius-2)

#draw the turtle masks
def mask(turtle, count, x, y, color, RADIUS, angle):
    turtle.penup()
    turtle.setx(x+1)
    turtle.sety(y)
    turtle.pendown()
    turtle.setheading(angle)

    turtle.color(color, color)
    turtle.begin_fill()
    turtle.forward(25)

    angle = alter_angle(angle, 60)
    turtle.setheading(angle)
    turtle.forward(25)
    
    angle = alter_angle(angle, 120)
    turtle.setheading(angle)
    turtle.forward(25)

    angle = alter_angle(angle, 60)
    turtle.setheading(angle)
    turtle.forward(25)
    turtle.end_fill()
    
    if count < 1:
        mask(turtle, count+1, x-RADIUS, y, color, RADIUS, -150)

def alter_angle(angle, amount):
    if angle < 0:
        return angle-amount
    else:
        return angle+amount
    

def main():
    ANIMATION_SPEED = 0

    #create background
    Screen().bgcolor("black")
    masterSplinter = Turtle()
    masterSplinter.color("#5aa8b9", "#5aa8b9")
    masterSplinter.up()
    masterSplinter.setpos(0, -400)
    masterSplinter.down()
    masterSplinter.begin_fill()
    masterSplinter.circle(400)
    masterSplinter.end_fill()

    #add the turtles!
    leonardo = Turtle()
    leonardo.speed(ANIMATION_SPEED)
    ninja(leonardo, "blue", -125, 125)

    donatello = Turtle()
    donatello.speed(ANIMATION_SPEED)
    ninja(donatello, "purple", 125, 125)

    michelangelo = Turtle()
    michelangelo.speed(ANIMATION_SPEED)
    ninja(michelangelo, "orange", -125, -125)

    raphael = Turtle()
    raphael.speed(ANIMATION_SPEED)
    ninja(raphael, "red", 125, -125)


main()
