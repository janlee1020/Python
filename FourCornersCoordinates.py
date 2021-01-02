#  FourCornersCoordinates.py
#  Janet Lee
#  Draw 4 circles in a window
#  Using setCoords instead of pixels

# import the graphics package
from graphics import *

#Greate a graphic window (using pixels)
win=GraphWin("Four Corners",400,200)

#Choose coordinate system
win.setCoords(0,0,4,2)

#Place a green circle in the upper right corner
upperRight=Circle(Point(3.7,1.7),.1)
upperRight.setFill("green")
upperRight.draw(win)

#Place a yellow circle in the upper left corner
upperRight=Circle(Point(.3,1.7),.1)
upperRight.setFill("yellow")
upperRight.draw(win)

#Place a red circle in the lower right corner
upperRight=Circle(Point(3.7,.3),.1)
upperRight.setFill("red")
upperRight.draw(win)

#Place a blue circle in the lower left corner
upperRight=Circle(Point(.3,.3),.1)
upperRight.setFill("blue")
upperRight.draw(win)

#Click the mouse to close the window.
win.getMouse()
win.close()
