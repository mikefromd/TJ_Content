from gturtle import *

def onMouseHit(x, y): 
    setPos(x, y)
    print(x, y)
    if x > -200 and x < 200:
        repeat 6: 
            dot(40)
            forward(60) 
            back(60) 
            right(60)

makeTurtle(mouseHit = onMouseHit)
speed(-1)
