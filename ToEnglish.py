# Official Name: Janet Lee
# Lab section: M3
# email: jlee67@syr.edu
# Assignment: Assignment 5, problem b.
# Date: Ocober 3, 2019
# Write a decoder function for pig latin

def main():
    #Ask for a file to decode and create the output file
    file=(input("Enter name of file with message to decode: "))
    out=file[:-4] + "Eng" + file[-4:]
    infile=open(file, "r")
    outfile=open(out, "w")
    print("The decoded message will be in", out)
    for line in infile:
        #Print sample dialogue
        print()
        print("Sample input file:", file)
        print(line)
        print()
        print("Sample output file:", out)
        for i in line.split():
            #Convert to English in all capital letters
            x=(i[-3]+i[:-3]+" ")
            y=x.upper()
            #Print results
            print(y, end="")
            print(y, end="", file=outfile)
    #Close output file
    outfile.close()

main()
