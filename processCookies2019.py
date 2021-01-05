#Janet Lee
#Lab M3
#processCookies.py
#Obtain information from the file cookieSales.txt.
#Print how many kids there are and their names.
#Print the total number of Samoas sold.

#From a line already read from a file, place the different
#    pieces of data in well named variables of a good type.
def getCookieData(aLine):
    aList=aLine.split()
    name=aList[0] + ' ' + aList[1]
    samoas=int(aList[3])  #notice int
    thinm=int(aList[2])
    shortb=int(aList[4])
    return name,thinm,samoas,shortb

def main():
    #open the input file
    infile=open("cookieSales2019.txt","r")
    #read the file into a list inputList
    inputList=infile.readlines()
    #compute how many kids there are
    numLines=len(inputList)
    numKids=numLines-2
    print("There are " + str(numKids) + " kids selling cookies.")  #notice str
    
    for i in range(numLines):
        print(inputList[i].rstrip())
        #print(inputList[i])


    
    #close and reopen to be back at the beginning of the file
    infile.close()
    infile=open("cookieSales2019.txt","r")  

    #read and ignore the header and the blank line
    infile.readline()
    infile.readline()
    #print the names of all the kids and compute the Samoas sales.
    sumThinm=0
    sumSamoas=0
    sumShortb=0
    for line in infile:
        name, thinm, samoas, shortb = getCookieData(line)
        sumThinm=sumThinm+thinm
        sumSamoas=sumSamoas + samoas   #notice int
        sumShortb=sumShortb+shortb
        print(name, "sold", thinm, "boxes of Thin Mint Cookies,", samoas, "boxes of Samoa Cookies, and", shortb, "boxes of Shortbread Cookies sold")

    #print the final total
    print("There were {0} boxes of Thin Mints sold.".format(sumThinm))
    print("There were {0} boxes of Samoas sold.".format(sumSamoas))
    print("There were {0} boxes of Shortbreads sold.".format(sumShortb))
    
#close the file
    infile.close()

main()

##There are 3 kids selling cookies.
##Name		Thin Mints	Samoas	Shortbreads
##
##Susie Fong	10		3	5
##Megan LaPlant	30		20	55
##Shoban Freeman	45		15	0
##Susie Fong sold 10 boxes of Thin Mint Cookies, 3 boxes of Samoa Cookies, and 5 boxes of Shortbread Cookies sold
##Megan LaPlant sold 30 boxes of Thin Mint Cookies, 20 boxes of Samoa Cookies, and 55 boxes of Shortbread Cookies sold
##Shoban Freeman sold 45 boxes of Thin Mint Cookies, 15 boxes of Samoa Cookies, and 0 boxes of Shortbread Cookies sold
##There were 85 boxes of Thin Mints sold.
##There were 38 boxes of Samoas sold.
##There were 60 boxes of Shortbreads sold.
