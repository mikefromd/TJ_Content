from gturtle import *

makeTurtle()
setPenColor('red')
setFillColor('yellow')
iteration = 0
angle = 150

startPath()
while True:
    forward(200)
    left(angle)
    iteration += 1
    print (str(iteration) + " " + str(getPos()))
    if int(distance(0,0)) <= 3:
        print (distance(0,0))
        break
fillPath()