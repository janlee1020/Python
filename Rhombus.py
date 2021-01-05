#Rhombus.py
#Janet Lee
#Lab 2 MW 2:15)
#Compute the area and perimeter of a rhombus

import math
def main():
    #Ask for the length of a side
    e = eval(input("Enter length of a side: "))

    #Ask for the length of the longer diagonal
    d = eval(input("Enter the length of the longer diagonal: "))

    #Compute the area and perimeter
    s= (2*e+d)/2
    area= 2*math.sqrt((s*(s-e)*(s-e)*(s-d)))
    perimeter= 4*e

    #Print the results
    print("area =", area, "square units")
    print("perimeter =", perimeter, "units")
                       
main ()
