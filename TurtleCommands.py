import turtle
import random

def reset():
    turtle.clear()

def setup():
    turtle.speed(100)
    turtle.screensize(1000, 800)

def drawRectangle(startx, starty, height, width, heading):
    turtle.penup()
    turtle.goto(startx, starty)
    turtle.setheading(heading)
    turtle.pendown()
    turtle.forward(height)
    turtle.right(90)
    turtle.forward(width)
    turtle.right(90)
    turtle.forward(height)
    turtle.right(90)
    turtle.forward(width)
    turtle.penup()

def rectanglePattern():
    startx = int(input("What is your starting X coordinate?"))
    starty = int(input("What is your starting y coordinate?"))
    height = int(input("what height do you want the rectangle? "))
    width = int(input("What width do you want the rectangle? "))
    drawRectangle(0,0,40,30,130)

def done():
    turtle.done()

def setRandomColor():
    x = random.randint(1,4)
    if x == 1:
        turtle.color("red")
    elif x == 2:
        turtle.color("blue")
    elif x == 3:
        turtle.color("orange")
    elif x == 4: 
        turtle.color("green")


