# Official Name: Janet Lee
# Lab section: M3
# email: jlee67@syr.edu
# Assignment: Assignment 4, problem 2.
# Date: September 21, 2019
# Plot points on graph paper

#Create a graph paper template
from graphics import *
def main():
    #Create a graphics window
    win=GraphWin("Graph Paper", 900, 500)
    win.setCoords(-10, -10, 26, 10)
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
    for i in range(21):
        blLine=Line(Point(-10+i, -10), Point(-10+i, 10))
        blLine.setFill("blue")
        blLine.draw(win)
    for i in range(21):
        blLine=Line(Point(-10, -10+i), Point(10, -10+i))
        blLine.setFill("blue")
        blLine.draw(win)
    #Create black tick marks that mark off multiples of 2
    for i in range(11):
        i=2*i
        tMark1=Line(Point(-10+i, -.5), Point(-10+i, .5))
        tMark1.setWidth(2)
        tMark1.draw(win)
    for i in range(11):
        i=2*i
        tMark2=Line(Point(-.5,-10+i), Point(.5, -10+i))
        tMark2.setWidth(2)
        tMark2.draw(win)
    #Label the axes
    xAx=Text(Point(8.5, .5), "x")
    xAx.draw(win)
    yAx=Text(Point(.5, 8.5), "Y")
    yAx.draw(win)

    #Input text
    lht=Text(Point(18,7),"Enter low and high values, then click mouse").draw(win)
    fVal=Text(Point(16,6),"First x value").draw(win)
    lVal=Text(Point(16,5),"Last x value").draw(win)

    #Add entry boxes
    fBox = Entry(Point(20, 6), 5)
    fBox.setText("-10")
    fBox.draw(win)
    hBox = Entry(Point(20, 5), 5)
    hBox.setText("10")
    hBox.draw(win)
    h=int(hBox.getText())
    #Have the user click the mouse
    win.getMouse()
    lht.undraw()

    #Add text and entry box
    f=int(fBox.getText())
    h=int(hBox.getText())
    xyVal=Text(Point(17.75, 4), ("x=", f, "y="))
    xyVal.draw(win)
    yBox = Entry(Point(20, 4), 5)
    yBox.setText("0")
    yBox.draw(win)

    #Plot points on graph
    x=1
    z=0
    f=f-1
    for i in range (f, h, 1):
        win.getMouse()
        x=x+1
        z=z+1
        xyVal.setText(("x=", (f+x), "y="))
        y=yBox.getText()
        aCircle = Circle(Point(f+z,y), .15)
        aCircle.setFill("yellow")
        aCircle.setOutline("green")
        aCircle.draw(win)
    
    #Close window
    cWin=Text(Point(18,2),"Click mouse to close window").draw(win)
    xyVal.undraw()
    win.getMouse()
    win.close()
    


main()
