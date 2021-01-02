#Janet Lee
#Lab M3
#Assessment 1A

def main():
    f=input("Food: ")
    o=eval(input("How many ounces in a portion? "))
    c=eval(input("How many calories in an ounce? "))
    tc=o*c
    print(f, "has", tc, "calories in a", o, "portion")
main()

#Food: Chocolate
#How many ounces in a portion? 3.5
#How many calories in an ounce? 143
#Chocolate has 500.5 calories in a 3.5 portion

#Food: Celery
#How many ounces in a portion? 2
#How many calories in an ounce? 2.86
#Celery has 5.72 calories in a 2 portion
    
