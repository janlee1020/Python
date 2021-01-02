# Official Name: Janet Lee
# Lab section: M3
# email: jlee67@syr.edu
# Assignment: Assignment 2, problem 2
# Date: September 10, 2019
# Compute the average of numbers inputted

def main():
    sum=0
    #Ask how many sample values
    num=eval(input("How many sample values? "))
    for n in range (1, num+1):
        print("value", n, ": ", end="")
        en=eval(input())
        #Compute sum and average
        sum=sum+en
        avg=sum/(num)
    #Print average
    print("Average:", avg)
                      
main()
                
