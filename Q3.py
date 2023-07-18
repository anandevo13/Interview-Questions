"""
Q. Convert characters of a string to opposite case
"""

# function to convert characters of a string to opposite case
def convertOpposite(str):
    ln = len(str)
    
    #Conversion according to ASCII values
    for i in range(ln):
        if str[i] >= 'a' and str[i] <= 'z':
            #Convert lowercase to uppercase
            str[i] = chr(ord(str[i]) - 32)
            
        elif str[i] >= 'A' and str[i] <= 'Z':
            #Convert lowercase to uppercase
            str[i] = chr(ord(str[i]) + 32)
            
#Driver Code
if __name__ == "__main__":
    str = "GeEkSfOrGeEkS"
    str = list(str)
    # calling the function
    convertOpposite(str)
    str = ''.join(str)
    print(str)
    
    
# Another method
# Python program to convert characters of string to opposite case
def convertString(str):
    length = len(str)
    result = ""
    for i in range(length):
        # If the character is in lowercase,
        # convert it to uppercase
        if str[i].islower():
            result += str[i].upper()
        # If the character is in uppercase,
        # convert it to lowercase
        elif str[i].isupper():
            result += str[i].lower()
        else:
            result += str[i]
    return result


str1 = "Welcome to MUO"
print("Original String 1:")
print(str1)
print("Converted String 1:")
print(convertString(str1))

# Another method: Using index(),without upper() and lower() methods   

# Python3 program to Convert characters
# of a string to opposite case

str = "GeEkSfOrGeEkS"
x = ""
lower="abcdefghijklmnopqrstuvwxyz"
upper="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
for i in str:
	if(i in upper):
		x += lower[upper.index(i)]
	elif(i in lower):
		x += upper[lower.index(i)]
print(x)


# Another method: Using numpy

import numpy as np

def convert_opposite_case(s):
     # Create a NumPy array from the string
     arr = np.frombuffer(s.encode('utf-8'), dtype='uint8').copy()

     # Find the indices of the alphabetic characters
     idx = np.where(np.logical_or(arr >= 65, arr <= 122))[0]

     # Toggle the case of each alphabetic character
     arr[idx] ^= 32

     # Convert the NumPy array back to a string
     return arr.tobytes().decode('utf-8')

print(convert_opposite_case('GeEkSfOrGeEkS'))

         
#Another Method: letter case toggling

# python program for the same approach
def isalpha(input):
    input_char = ord(input[0])
 
    # CHECKING FOR ALPHABET
    if((input_char >= 65 and input_char <= 90) or (input_char >= 97 and input_char <= 122)):
        return True
    else:
        return False
 
#Another method: Function to toggle characters
 
def toggleChars(S):
    s = ""
 
    for it in range(len(S)): 
        if(isalpha(S[it])):
            s += chr(ord(S[it]) ^ (1 << 5))
        else:
            s += S[it]
    return s
 
# Driver code
S = "GeKf@rGeek$"
print(toggleChars(S))


#Another Method:

# Python3 program to Convert characters of a string to opposite case
str = "GeEkSfOrGeEkS"
x = ""
for i in str:
    if(i.isupper()):
        x += i.lower()
    else:
        x += i.upper()
print(x)


#Another Method: Using swapcase() function

# Python3 program to Convert characters of a string to opposite case
str = "GeEkSfOrGeEkS"

print(str.swapcase())


#Another Method: Use re:

import re
 
def convert_opposite_case(s):
    # Define regular expression pattern for alphabetic characters
    pattern = r'[a-zA-Z]'
 
    # Replace each character with its opposite case
    s = re.sub(pattern, lambda x: x.group().lower()
               if x.group().isupper() else x.group().upper(), s)
    return s
 
print(convert_opposite_case('GeEkSfOrGeEkS'))


# Aother Method: Using reduce() function and lambda expression:

from functools import reduce
str = "GeEkSfOrGeEkS"
result = reduce(lambda x, y: x+y.lower() if y.isupper() else x+y.upper(), str, "")
print(result)
 
         