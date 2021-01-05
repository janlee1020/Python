#Janet Lee
#Lab M3
#Months.txt

longMonth=["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
month= int(input("Input a month number: "))
longMonth=longMonth[month-1]
daysMonth=["31", "28", "31", "30", "31", "30", "31", "31", "30", "31", "30", "31"]
daysMonth=daysMonth[month-1]
print(longMonth, "has", daysMonth, "days") 
