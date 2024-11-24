# Starter Code
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

operation = input("Enter 'encode' to encrypt the text or 'decode' to find out the text!\n").lower()
text = input("Enter the text to encode\n").lower()
shift = int(input("Enter the number of characters to shift\n"))

# Write your code below

#TODO Create a function called caesar that will combine both encode and decode into one
#TODO Using a for loop we will determine what shift to apply depending on the operation
# Example: If operation is encode + shift, decode is - shift
#TODO To change the shift check for the operation decode since it is going to use a negative 
#TODO Print the completed text using an f-string