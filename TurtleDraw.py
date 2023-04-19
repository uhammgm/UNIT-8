from TurtleCommands import *
import time

while True:
    setup()
    setRandomColor()
    drawCirclePattern()
    time.sleep(5)
    reset()
    response = input("Do you want to quit? ")
    if response == "y":
        break

done()
