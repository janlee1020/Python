# Official Name:  Janet Lee
# email:  jlee67@syr.edu
# Assignment: Assignment 6, problem B.
# Date:  Ocotober 13, 2019
# Click a colored rectangle and have the triangle become that color
from graphics import *
#Create the graphics

def checkButtonClick(clickedPoint, rightLower, leftUpper):
    xValue=clickedPoint.getX()
    yValue=clickedPoint.getY()
    if (xValue<=rightLower.getX() and xValue>=leftUpper.getX() and yValue<=leftUpper.getY() and yValue>=rightLower.getY()):
        return "in"
    else:
        return "out"
    
def main():
    win= GraphWin("4 Rectangles and Triangle", 700, 700)
    win.setCoords(0, 0, 7, 7)
    #Draw a triangle
    aTriangle=Polygon(Point(3,3), Point(3.75,4), Point(4.5,3))
    aTriangle.draw(win)
    #Draw a yellow rectangle
    yRect=Rectangle(Point(0.5, 5.5), Point(2, 6.5))
    yRect.setFill("yellow")
    yRect.draw(win)
    ymessage=Text(Point(1.25, 6), "Yellow")
    ymessage.draw(win)
    #Draw a blue rectangle
    bRect=Rectangle(Point(5, 5.5), Point(6.5, 6.5))
    bRect.setFill("blue")
    bRect.draw(win)
    bmessage=Text(Point(5.75, 6), "Blue")
    bmessage.draw(win)
    #Draw a red rectangle
    rRect=Rectangle(Point(5, 0.5), Point(6.5, 1.5))
    rRect.setFill("red")
    rRect.draw(win)
    rmessage=Text(Point(5.75, 1), "Red")
    rmessage.draw(win)
    #Draw a purple rectangle
    pRect=Rectangle(Point(0.5, 0.5), Point(2, 1.5))
    pRect.setFill("purple")
    pRect.draw(win)
    pmessage=Text(Point(1.25, 1), "Purple")
    pmessage.draw(win)
    #Get mouse
    count = 10
    countdown=Text(Point(3.5, 6.75), count)
    countdown.draw(win)
    for i in range(10):
        clickedPoint=win.getMouse()
        count=count-1
        print(count)
        countdown.setText(count)
        
    #Draw yellow triangle if getMouse() is in the yellow rectangle
        yt = checkButtonClick(clickedPoint, Point(2, 5.5), Point(.5, 6.5))
        print(yt)
        if yt == "in" :
            aTriangle.setFill("yellow")

   #Draw blue triangle if getMouse() is in the blue rectangle
        elif checkButtonClick(clickedPoint, Point(6.5, 5.5), Point(5, 6.5))== "in" :
            aTriangle.setFill("blue")

    #Draw red triangle if getMouse() is in the red rectangle
        elif checkButtonClick(clickedPoint, Point(6.5, .5), Point(5, 1.5))== "in" :
            aTriangle.setFill("red")
    
    #Draw purple triangle if getMouse() is in the purple rectangle
        elif checkButtonClick(clickedPoint, Point(2, .5), Point(.5, 1.5))== "in" :
            aTriangle.setFill("purple")

        else:
            aTriangle.setFill("white")
            
    win.getMouse() 
    win.close()

        
main()
