from TurtleCommands import *
import time

while True:
    print("~~~~~~~Selection Menu~~~~~~~")
    Ans = 0
    Ans = int(input("1. Draw Square\n2. Draw Circle\n3. Draw Super Pattern  "))
    if Ans == 1:
        setup()
        setRandomColor()
        rectanglePattern()
        time.sleep(5)
        reset()
        response = input("Do you want to quit? ")
        if response == "y":
            break
    elif Ans == 2:
        setup()
        setRandomColor()
        drawCirclePattern()
        time.sleep(5)
        reset()
        response = input("Do you want to quit? ")
        if response == "y":
            break
    elif Ans == 3:
        setup()
        setRandomColor()
        drawSuperPattern()
        time.sleep(5)
        reset()
        response = input("Do you want to quit? ")
        if response == "y":
            break

done()
