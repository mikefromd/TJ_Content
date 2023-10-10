from gturtle import *

makeTurtle()

setPenColor("red")
setLineWidth(3)

setFillColor("black")
startPath()
repeat(3):
    forward(100)
    left(120)
fillPath()