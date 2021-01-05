#shapeCalculator.py
from math import pi

def rectArea(length, width):
    area=length * width
    return area

def circleArea(radius):
    area=pi*radius*radius
    return area

def welcome():
    print("Welcome to the shape calculator!")
    name=input("What is your name? ")
    return name

def askDimension(dimension):
    value = float(input("what is the " + dimension +"? "))
    return value

def triangleArea(altitude, base):
    x=altitude
    y=base
    area=(1/2)*altitude*base
    return area
    
def squareArea(side):
    s=length
    area=s**2
    return area
    
def main():
    name = welcome()
    print(name+", ", end="")
    x = askDimension("length")  #enter 4
    y = askDimension("width")   #enter 3

    print("The area of the rectangle is " + str(rectArea(x,y)))
    
    rad = askDimension("radius")   #enter 10
    a= circleArea(rad)
    print("The area of the circle is {0:0.5} sq. cm.".format(a))
    
    print("The area of the triangle is " + str(triangleArea(x,y)))

    print("The area of the square is " + str(rectArea(x, x)))

    #Compute and print area of a square from dimList
    dimList=[5, 3, 7, 2]
    sqarea=int(dimList[0]) ** 2
    print("The area of the square from dimList is ", sqarea)
    #Compute and print area of a circle from dimList
    circarea= (int(dimList[1])**2)*pi
    print("The area of the circle from dimList is ", circarea)
    #Compute and print area of a rectangle from dimList
    recarea=int(dimList[2])* int(dimList[3])
    print("The area of the rectangle from dimList is ", recarea)
main()

##Output
##Welcome to the shape calculator!
##What is your name? Janet
##Janet, what is the length? 4
##what is the width? 3
##The area of the rectangle is 12.0
##what is the radius? 10
##The area of the circle is 314.16 sq. cm.
##The area of the triangle is 6.0
##The area of the square is 16.0
##The area of the square from dimList is  25
##The area of the circle from dimList is  28.274333882308138
##The area of the rectangle from dimList is  14

