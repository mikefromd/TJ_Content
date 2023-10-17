from gpanel import *

size = 300

makeGPanel(Size(2 * size, size))
window(0, 2 * size, size, 0)    # y axis downwards
lineWidth(10)
move(50,50)
setColor("black")
draw(500,50)
setColor("red")
draw(500, 250)
setColor("green")
draw(50, 250)
setColor("purple")
draw(50, 50)