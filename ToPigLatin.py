# Official Name: Janet Lee
# Lab section: M3
# email: jlee67@syr.edu
# Assignment: Assignment 5, problem A.
# Date: Ocober 3, 2019
# Write an encoder function for pig latin

def main():
    print("Sample dialogue: ")
    file=(input("Enter name of file with message to encode: "))
    out=file[:-4] + "PL" + file[-4:]
    infile=open(file, "r")
    outfile=open(out, "w")
    print("The output is in the file", out)
    a="ay"
    for line in infile:
        print()
        print("Sample input file:", file)
        print(line)
        print()
        print("Sample output file:", out)
        for i in line.split():
            x=(i[1:]+ i[0]+a+ " ")
            y=x.lower()
            print(y, end="")
            print(y, end="", file=outfile)
    outfile.close()
    
            
main()


