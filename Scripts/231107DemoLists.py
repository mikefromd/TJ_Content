# Small test with turtle graphic and lists
# The default playground's coordinates are 
# -300 to 300 (x, horizontal size) and 
# -200 to 200 (y, vertical size)

from gturtle import *

# Just a one dimensional list
testList = [12, 34, 56, 61, 2]    # list with 5 elements at the beginning/initialisation
print testList[1]    # prints 34, attention first element has index 0
print (str(testList[2] + testList[3]))


# Apply a two dimensional list to hold coordinates (x,y)
makeTurtle("red")

# 3 coordinate points
coordinates = [[100,100], [200, 200], [300, 100]]

setPenColor("brown")
for i in range(3):
    moveTo(coordinates[i])
    dot(25)

# Better way to iterate over all points
setPenColor("green")
for xy in coordinates:
    moveTo(xy)
    dot(25)