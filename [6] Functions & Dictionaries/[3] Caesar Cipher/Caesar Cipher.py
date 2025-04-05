# Starter Code
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

operation = input("Enter 'encode' to encrypt the text or 'decode' to find out the text!\n").lower()
text = input("Enter the text to encode\n").lower()
shift = int(input("Enter the number of characters to shift\n"))

# Write your code below

#TODO Complete the tasks below!
"""
» NOTE Use the index() function to find the position of a letter in the list

» Create a function named encrypt that will take text and shift as parameters
» 
"""

#NOTE Use the index() function to find the position of an element within a list
#TODO Create a function called encrypt that takes text and shift as parameters
#TODO Inside the encrypt function shift each letter of the text using the parameter
"""
Example:
    text = "hello"
    shift = 3

    encoded text = "khoor"
"""

#TODO Create a function called decrypt that will decode the encoded text
#TODO Inside the decrypt function shift every letter back to get the original text
"""
Example:
    text = "khoor"
    shift = 3

    encoded text = "hello"
"""

#TODO Create a match case to detect what operation the user wants and call the appropriate functions