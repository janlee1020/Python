# Official Name: Janet Lee
# Lab section: M3
# email: jlee67@syr.edu
# Assignment: Assignment 3, problem 2.
# Date: September 16, 2019
# Compute and print the result of the sum of a series


def main():
    d, n=eval(input("enter denominator and the number of terms: "))
    sum=0
    for k in range (1, n+1):
        sum=sum+1/(d**k)
        print(k, "", sum)
    print("sum = ", sum)
    e=(1/(d-1))
    r=e-sum
    print("(1 /", d-1, ")", "- sum =", r)
main()
