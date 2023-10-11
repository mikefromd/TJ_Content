from gturtle import *

Oscar = makeTurtle()

Oscar.setPenColor("red")
Oscar.setLineWidth(3)

Oscar.setFillColor("black")

repeat(3):
    Oscar.forward(100)
    Oscar.left(120)

Oscar.penUp()
Oscar.left(45)
Oscar.forward(20)
Oscar.fill()