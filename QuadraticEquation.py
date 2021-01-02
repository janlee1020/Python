#Janet Lee
#Lab M3
#Assessment 3B

def quadEquation(x,a,b):
    y=(a*(x)**2)+b
    return y

def main():
    a=int(input("Enter Coefficient a: "))
    b=int(input("Enter Coefficient b: "))
    for i in range(1,6):
        y=quadEquation(i,a,b)
        print("x=", i, "a=", a, "b=", b, "y=", y)

main()

##Output
##Enter Coefficient a: 12
##Enter Coefficient b: 20
##x= 1 a= 12 b= 20 y= 32
##x= 2 a= 12 b= 20 y= 68
##x= 3 a= 12 b= 20 y= 128
##x= 4 a= 12 b= 20 y= 212
##x= 5 a= 12 b= 20 y= 320
##Enter Coefficient b: 11
##x= 1 a= 5 b= 11 y= 16
##x= 2 a= 5 b= 11 y= 31
##x= 3 a= 5 b= 11 y= 56
##x= 4 a= 5 b= 11 y= 91
##x= 5 a= 5 b= 11 y= 136
##Enter Coefficient a: 3
##Enter Coefficient b: 4
##x= 1 a= 3 b= 4 y= 7
##x= 2 a= 3 b= 4 y= 16
##x= 3 a= 3 b= 4 y= 31
##x= 4 a= 3 b= 4 y= 52
##x= 5 a= 3 b= 4 y= 79
