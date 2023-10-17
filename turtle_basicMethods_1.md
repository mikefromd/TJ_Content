# gturtle - some basic methods 2.1 to 2.8

The name of the parameters contains an indication on what type of parameter is required.
- ...Int... -> Integer
- ...Float... -> Float
- ...Num... -> Integer of Float
- ...String... -> Textstring, using '...' or "..." 


| Method | Description |
|:--------------------|-----------------------------|
| **Initialisation & Operation** | |
| makeTurtle() | creates a (global) turtle and defines all global commands; default size is 800 x 600, (0,0) in the centre  |
| makeTurtle(aColorString)  | same, but creates a turtle with a given color  |
| makeTurtle("sprites/aSpriteNameString") |  same, but creates a turtle with given sprite image, check the library for a sprite  |
| | |
| speed(anInt) | sets the speed of the turtle movement to anInt |
| hideTurtle() | Speeds up drawing process |
| showTurtle() | shows turtle (drawing)
| | |
| **Movements** | |
| back(aNum) | move the turtle backwards for the distance aNum |
| forward(aNum) | move the turtle forward for the distance aNum |
| left(aNum) | turns turtle aNum degrees to the left |
| right(aNum) | turns turtle aNum degrees to the right |
| penDown() | puts pen down, turtle will draw afterwards |
| penUp() | lifts the pen, further movements will not show on the playground |
| leftCircle(aNumRadius) | Draw a circle with its centre at the present location of the turtle with radius aNumRadius |
| | |
| **Positioning** | |
| setPos(xNum, yNum) | Move the turtle to the coordinates (xNum, yNum) |
| direction(xInt, yInt) | returns the angle to turn to the position (xInt, yInt) |
| distance(xInt, yInt) | returns the distance of the turtle to point (xInt, yInt) |
| leftArc(aNumRadius, aNumAngle) | moves the turtle on a left oriented arc with radius aNumRadius and sector angle aNumAngle |
| rightArc(aNumRadius, aNumAngle) | similar to leftArc, but right-turn |
| setRandomPos(xPosNum, yPosNum) | move the turtle to a random position within the given rectangle of size (xPosNum, yPosNum), centered around (0,0).
| | |
| **Colour**  | |
| setPenColor("aColourString") | Set the pen colour, aColorString can be any X11 colour |
| setFillColor("aColorString") | Define the fill colour applied ito the area drawn by a turtle position (turtle not touching the lines) or defined by the code between a startPath() and fillPath() method. |
| askColor("aStringTitle", "aDefaultColorString") | Opens a window with name aStringTitle that lets the user choose a colour, aDefaultColorString is selected if no choice is made. The return value of the function can be saved in a varialbe for further processing. |
| fillToPoint(xPosNum, yPosNum) | fills continously from the given point |
| fillToHorizontal(yPosNum) | Fills continously the area defined by the given y coordinate yPosNum and the y position of the turtle. |
| dot(aNumDiameter) | Draw a dot of diameter aNumDiameter at the position of the turtle |
| | |
| **Data Input and Output** | |
| inputInt("aPromptString") | This function opens a window, displaying the aPromptString asking for the input of a integer. You can assign a variable `aVar = inputInt("aPromptString") to get the entered value and then process it in the program. |



