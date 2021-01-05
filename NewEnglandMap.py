# Official Name: Janet Lee
# email: jlee67@syr.edu
# Assignment: Assignment 6, problem B.
# Date: October 7, 2019
# Create a map of the surrounding states of New England
from graphics import *
def main():
    infile=open("NewEngland.txt", "r")
    header=infile.readline()
    #Create graphic window
    win= GraphWin("New England", 700, 700)
    win.setBackground("light blue")
    win.setCoords(-1, -1, 9, 9)
    for line in infile:
        ht, wd = setDimensions(line)
        xL, yL = setLowerLeft(line)
        name, color = setNameAndColor(line)
        xU, yU = upperCoords(xL, yL, wd, ht)
        yRect=Rectangle(Point(xL, yL), Point(xU, yU))
        yRect.setFill(color)
        yRect.draw(win)
        xM, yM=setMidpoint(xL, yL, xU, yU)
        aTex=Text(Point(xM, yM), name)
        aTex.draw(win)

def setDimensions(list):
    list=list.split()
    ht=float(list[1])
    wd=float(list[2])
    return ht, wd

def setLowerLeft(list):
    list=list.split()
    xL=float(list[3])
    yL=float(list[4])
    return xL, yL

def setNameAndColor(list):
    list=list.split()
    name=str(list[0])
    color=str(list[5])
    return name, color
 
def upperCoords(xL,yL,wd,ht):
    xU=xL+wd
    yU=yL+ht
    return xU, yU
  
def setMidpoint(xL,yL,xU,yU):
    xM=(xL+xU)/2
    yM=(yL+yU)/2
    return xM, yM

main()
