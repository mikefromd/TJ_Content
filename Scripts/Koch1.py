from gturtle import *

makeTurtle()
speed(1000)

def koch(order, size):
    """
       The turtle draws a Koch fractal of given order and size.
    """
    
    if order == 0:
        forward(size)
    else:
        koch(order-1, size/3)
        left(60)
        koch(order-1, size/3)
        right(120)
        koch(order-1, size/3)
        left(60)
        koch(order-1, size/3)
    
    
order = 1
size = 200

repeat(1):
    koch(order, size)
    right(120)
