import turtle
import random

def reset():
    turtle.clear()

def setup():
    turtle.speed(100)
    turtle.screensize(1000, 800)

def drawRectangle(startx, starty, height, width, heading, offset):
    turtle.penup()
    turtle.goto(startx, starty)
    turtle.setheading(heading)
    turtle.penup()
    turtle.forward(offset)
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
    startx = int(input("What is your starting X coordinate? "))
    starty = int(input("What is your starting y coordinate? "))
    height = int(input("what height do you want the rectangle? "))
    width = int(input("What width do you want the rectangle? "))
    count = int(input("How many rectangles do you want? "))
    angChange = int(360 / count)
    offset = int(input("Offset of the circle (radius) "))
    heading = 0
    x = 0

    while x < count: 
        turtle.goto(startx, starty)
        heading = heading + angChange
        drawRectangle(startx,starty,height,width,heading,offset)
        setRandomColor()
        x += 1
        
def drawCirclePattern():
    startx = int(input("What is your starting X coordinate? "))
    starty = int(input("What is your starting y coordinate? "))
    count = int(input("How many circles? "))
    offset = int(input("Offset of the circle (radius) "))
    rad = int(input("What is the radius of your circles? "))
    x = 0
    angChange = 360 / count
    heading = 0
    while x < count:
        setRandomColor()
        turtle.goto(startx, starty)
        heading = heading + angChange
        turtle.setheading(heading)
        turtle.penup()
        turtle.forward(offset)
        turtle.pendown()
        turtle.circle(rad)
        turtle.penup()
        x += 1

def drawSuperPattern():
    import random

    count = random.randint(10,50)
    
    x = 0
    y = 0
    angChange = 360 / count
    heading = 0
    choice = 0
    while y < count:
        choice = random.randint(1,2)
        if choice == 1:
            startx = 0
            starty = 0
            offset = random.randint(100,500)
            rad = random.randint(100, 500)
            setRandomColor()
            turtle.goto(startx, starty)
            heading = heading + angChange
            turtle.setheading(heading)
            turtle.penup()
            turtle.forward(offset)
            turtle.pendown()
            turtle.circle(rad)
            turtle.penup()
            y += 1
        elif choice == 2:
            height = random.randint(100, 600)
            width =- random.randint(100, 600)
            turtle.goto(startx, starty)
            heading = heading + angChange
            drawRectangle(startx,starty,height,width,heading,offset)
            setRandomColor()
            y += 1
            

            


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