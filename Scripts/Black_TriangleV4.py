from gturtle import *

tf = TurtleFrame()

Oscar = Turtle(tf)
Maya = Turtle(tf)
Oscar.setPos(-100, -100)
Maya.setPos(100, 100)

Oscar.setPenColor("red")
Oscar.setLineWidth(3)
Oscar.setFillColor("black")

Maya.setPenColor("cyan")
Maya.setLineWidth(5)
Maya.setFillColor("orange")

repeat(3):
    Oscar.forward(100)
    Oscar.left(120)
    Maya.forward(100)
    Maya.left(120)

Oscar.penUp()
Oscar.left(45)
Oscar.forward(20)
Oscar.fill()