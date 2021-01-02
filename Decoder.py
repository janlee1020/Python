# Official Name: Janet Lee
# Lab section: M3
# email: jlee67@syr.edu
# Assignment: Assignment 4, problem 1.
# Date: September 21, 2019
# Decode a simple code

def main():
    message=""
    rMessage=""
    alphabet="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    #Ask how many letters in a message
    m=int(input("How many letters in a message? "))
    for i in range(m):
        c=int(input("next code value: "))
        c=str(alphabet[c-1])
        message=message+c
        rMessage=c+rMessage
        
    print("Decoded Message before reverse: ", message)
    print("Decoded Message: ", rMessage)
main()
#Trial 1
#How many letters in a message? 6
#next code value: 14
#next code value: 15
#next code value: 8
#next code value: 20
#next code value: 25
#next code value: 16
#Decoded Message before reverse:  NOHTYP
#Decoded Message:  PYTHON

#Trial 2
#How many letters in a message? 3
#next code value: 2
#next code value: 1
#next code value: 5
#Decoded Message before reverse:  BAE
#Decoded Message:  EAB

#Trial 3
#How many letters in a message? 4
#next code value: 1
#next code value: 2
#next code value: 3
#next code value: 4
#Decoded Message before reverse:  ABCD
#Decoded Message:  DCBA
