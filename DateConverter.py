#Janet Lee
#Lab M3
#DateConverter.py

def main():
    #Ask for a number corresponding to a month
    months="JanFebMarAprMayJunJulAugSepOctNovDec"
    numDate=input("Input a date in the form mm/dd/yy: ")
    k=int(numDate[0:2])
    pos=3*k-3
    #Get the month, day, and year
    monthAbbrev=months[pos:pos+3]+"."
    numDay=int(numDate[3:5])
    numYear="20"+ numDate[6:8]
    #Print results
    print(monthAbbrev, numDay, numYear)

main()
    
