# Official Name: Janet Lee
# Lab section: M3
# email: jlee67@syr.edu
# Assignment: Assignment 2, problem 1.
# Date: September 10, 2019
# Compute a receipt for Gracie's Garden Store

print("Welcome to Gracie's!")
print("Let the sun shine in!")
print()
print("For each item, enter the quantity, then press ENTER")

import math
def main():
    #Ask for number of pansies
    p=eval(input("PANSIES:"))
    #Compute cost of total pansies
    dp=(p//12)
    sp=(p%12)
    tpc=((6.5*(dp))+(.58*(sp)))
    #Ask for number of tulip bulbs
    tb=eval(input("TULIP BULBS:"))
    #Compute cost of total tulip bulbs
    qtb=(tb//4)
    stb=(tb%4)
    ttbc=((2.5*(qtb))+(.7*(stb)))
    #Ask for number of rose bushes
    rb=eval(input("ROSE BUSHES:"))
    #Compute cost of total rose bushes
    trb=(rb//3)
    srb=(rb%3)
    trbc=((20*(trb))+(8.5*(srb)))
    #Ask for number of begonias
    b=eval(input("BEGONIAS:"))
    #Compute cost of total begonias
    db=(b//2)
    sb=(b%2)
    tbc=((30*(db))+(17*(sb)))
    #Ask for number of hydrangeas
    h=eval(input("HYDRANGEAS:"))
    #Compute cost of total hydrangeas
    qh=(h//4)
    sh=(h%4)
    thc=((120*(qh))+(32*(sh)))
    #Compute total number of flowers and total cost
    tf=p+tb+rb+b+h
    tc=tpc+ttbc+trbc+tbc+thc
    print()
    print()
    print("Your Receipt")
    print("PANSIES","\t", p, "\t", "$", tpc)
    print("TULIP BULBS", "\t", tb, "\t", "$", ttbc)
    print("ROSE BUSHES", "\t", rb, "\t", "$", trbc)
    print("BEGONIAS","\t", b, "\t", "$", tbc)
    print("HYDRANGEAS","\t", h, "\t", "$", thc)
    print("----------------------------------------------------")
    print("TOTAL","\t","\t", tf, "\t", "$", tc)

main ()

