# Starter Code
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input("How many symbols would you like?\n"))
nr_numbers = int(input("How many numbers would you like?\n"))

difficulty = input("Easy password or hard password?\n").lower()
password = ""


# Write your code below!


# TODO Complete the tasks below!
"""
» Create a match case to check if the user wants an easy or hard password, check for invalid inputs
» Create a for loop that randomly chooses elements from the lists
» Add each chosen element to the password variable
» Use the _ instead of an iterator variable to choose a random element from the lists using random.choice()
» Easy Level Password
    › Not randomized order of characters
    › Example: 4 letters, 2 symbols, 2 numbers = JduE&!91
    › Print the password using an f-string
» Hard Level Password
    › Randomized order of characters
    › Example: 4 letters, 2 symbol, 2 number = g^2jk8&P
    › Create en empty list to store the characters generated
    › Use shuffle() to shuffle the characters and add them into the password
    › Print the password using an f-string
"""