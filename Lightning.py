# Official Name: Janet Lee
# Lab section: M3
# email: jlee67@syr.edu
# Assignment: Assignment 3, problem 1.
# Date: September 14, 2019
# Compute the time lapse of seeing to hearing a lightning strike

def main():
    #Ask user how many lines
    l= eval(input("How many lines do you want in your table? "))
    #Print headers
    print("Time", "\t", "Distance", "\t", "Distance")
    print("seconds", "feet", "\t","\t", "miles")
    #Compute time lapse
    sum=0
    for i in range (0, 5*l, 5):
        sum=sum+(i/10)
        s=1100*i/10
        m=s/5280
        #Print results
        print(i/10, "\t", s, "\t", "\t", m)
        
main()
    
