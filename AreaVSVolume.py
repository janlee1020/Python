# Official Name: Janet Lee
# Lab section: M3
# email: jlee67@syr.edu
# Assignment: Assignment 2, problem 3
# Date: September 10, 2019
# Compare how the volume of a sphere grows with the increase of the surface area

import math
def main ():
    #Ask what the largest radius would be
    lr=eval(input("What is the largest radius you want to consider?"))
    #Print the column titles
    print("radius", "\t", "\t", "surface area", "\t", "\t", "volume", "\t", "\t", "ratio")
    #Compute surface area, volume, and ratio
    for r in range(1, lr+1):
        sa=4*(math.pi)*(r**2)
        v=(4/3)*(math.pi)*(r**3)
        rat=v/sa
        #Print results
        print(r, "\t", sa, "\t", v, "\t", rat)
    
main()

    
    
