#code.py
#encoding and decoding using Unicode

# This program is based on numbers2text.py in Zelle chapter 5
def numbers2text():
    #Get the message to encode
    inString = input("Please enter the Unicode-encoded message: ")
    
    #Loop through each substring and build Unicode message
    message=""
    for numStr in inString.split():
        codeNum = int(numStr)            # convert digits to a number
        message = message + chr(codeNum) #concatenate character to message
        
    print("\nThe decoded message is: ", message)
    #end numbers2text()
    
# This program is based on text2numbers.py in Zelle chapter 5
# A method to convert a textual message into a sequence of numbers
#   utilizing the underlying Unicode encoding
def text2numbers():
    # Get the message to encode
    message = input("Please enter the message to encode: ")
    
    print("Here are the Unicode codes: ")
    
    # Loop through the message and print out the Unicode values
    for ch in message:
        print(ord(ch), end=" ")
        
    print()    # blank line before shell prompt
    #end text2numbers()
numbers2text()

              
