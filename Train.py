# Official Name: Janet Lee
# Lab section: M3
# email: jlee67@syr.edu
# Assignment: Assignment 3, problem 3.
# Date: September 16, 2019
# Create a drawing of a train

from graphics import *
def main():
#Create a blue graphic window

    win= GraphWin("Train", 500, 300)
    win.setBackground("blue")
    win.setCoords(0, 0, 5, 3)
    #Print title
    message=Text(Point(2.5, 2.75), "Grayte Train")
    message.setTextColor("black")
    message.setStyle("bold")
    message.draw(win)
    #Create a polygon for the car
    pPoly=Polygon(Point(0.75, 0.75), Point(0.75, 1.25), Point(1.25, 1.25), Point(1.25, 2.25), Point(4, 2.25), Point(4, 1.25), Point(4.5, 1.25), Point(4.5, 0.75))
    pPoly.setFill("gray")
    pPoly.draw(win)

    #Place two black circles for wheels
    bCircle=Circle(Point(1.5, 0.75), 0.4)
    bCircle.setFill("black")
    bCircle.draw(win)
    b2Circle=Circle(Point(3.75, 0.75), 0.4)
    b2Circle.setFill("black")
    b2Circle.draw(win)

#Use a loop to create 6 yellow rectangular windows
    for x in range(6):
        x= 0.4*x+0.05
        yRect=Rectangle(Point(1.5+x, 1.5), Point(1.65+x, 1.75))
        yRect.setFill("yellow")
        yRect.draw(win)
#Click the mouse to change the graphics window color to light blue
    win.getMouse()
    win.setBackground("cyan")
#Click the mouse to close the window
    win.getMouse()
    win.close()

main()
