from TurtleCommands import *
import time

while True:
    setup()
    setRandomColor()
    rectanglePattern()
    time.sleep(2)
    reset()
    response = input("Do you want to quit? ")
    if response == "y":
        break

done()
