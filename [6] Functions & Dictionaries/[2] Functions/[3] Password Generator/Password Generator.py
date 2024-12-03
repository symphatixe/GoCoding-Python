# Starter Code
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
password = ""


# Write your code below!

#TODO Create a function called generate that takes some number of characters as well as the difficulty of the password
#TODO Using the two parameters it will generate a password based on the instructions below
#NOTE Remember to randomize between the different lists and enter a random character from the list into the list.
#TODO Check the difficulty of the password and shuffle the characters if needed
#TODO Create a function called main() that encapsulates the input() logic and the function call.
# The main() is useful because we want to separate the function definition from the logic that the user sees.

#Easy Level - Order not randomized:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91

#Hard Level - Order of characters randomized:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P