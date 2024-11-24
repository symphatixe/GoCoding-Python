# Starter Code
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

operation = input("Enter 'encode' to encrypt the text or 'decode' to find out the text!\n").lower()
text = input("Enter the text to encode\n").lower()
shift = int(input("Enter the number of characters to shift\n"))

# Write your code below

#TODO Create a function called encrypt that takes text and shift as parameters
#TODO Inside the encrypt function shift each letter of the text using the parameter
"""
Example:
    text = "hello"
    shift = 3

    encoded text = "khoor"
"""