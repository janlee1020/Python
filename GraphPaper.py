# Official Name: Janet Lee
# Lab section: M3
# email: jlee67@syr.edu
# Assignment: Assignment 4, problem 2.
# Date: September 21, 2019
# a brief description of the problem.
#Create a graph paper template
from graphics import *
def main():
    #Create a graphics window
    win=GraphWin("Graph Paper", 700, 700)
    win.setCoords(-10, -10, 10, 10)
    #Draw black lines for the axes
    bLine=Line(Point(0, 10), Point(0, -10))
    bLine.setFill("black")
    bLine.setWidth(3)
    bLine.draw(win)
    bLine2=Line(Point(-10, 0), Point(10, 0))
    bLine2.setFill("black")
    bLine2.setWidth(3)
    bLine2.draw(win)
    #Create horizontal and vertical blue lines for every half unit
    for i in range(20):
        blLine=Line(Point(-10+i, -10), Point(-10+i, 10))
        blLine.setFill("blue")
        blLine.draw(win)
    for i in range(20):
        blLine=Line(Point(-10, -10+i), Point(10, -10+i))
        blLine.setFill("blue")
        blLine.draw(win)
    #Create black tick marks that mark off multiples of 2
    for i in range(10):
        i=2*i
        tMark1=Line(Point(-10+i, -.5), Point(-10+i, .5))
        tMark1.setWidth(2)
        tMark1.draw(win)
    for i in range(10):
        i=2*i
        tMark2=Line(Point(-.5,-10+i), Point(.5, -10+i))
        tMark2.setWidth(2)
        tMark2.draw(win)
    #Label the axes
    xAx=Text(Point(8.5, .5), "x")
    xAx.draw(win)
    yAx=Text(Point(.5, 8.5), "Y")
    yAx.draw(win)
    
    


main()
