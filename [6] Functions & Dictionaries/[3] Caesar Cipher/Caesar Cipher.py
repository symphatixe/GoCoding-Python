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
    › Create an empty string to store the text that will be changed
    › Using a for loop, go over each letter to shift it using index()
    › Add the shifted letters to the empty string
    › Print out the original text and the encrypted text using an f-string
» Repeat the same steps for the decrypt function, but use different parameters
    › Namely: encoded_text and shift instead of text and shift
» Create a match case to detect what operation the user wants and call the appropriate functions
"""