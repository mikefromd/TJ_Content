from gturtle import *

makeTurtle()

def myFunctionSquares(size, xPos, yPos):
    setPos(xPos, yPos)
    fillToPoint(xPos,yPos)
    repeat 4:
        forward(size)
        left(90)
    return("All well!")

# Main Program
returnVal = myFunctionSquares(200, -150, -50)
print(returnVal)