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

#TODO Create a set of conditionals to detect whether the user chooses the easy or hard password and
# check for invalid inputs

#Easy Level - Order not randomized:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91

#TODO Using the _ instead of an iterator variable in for loops choose a random
# element from the list using choice() with the lists as a parameter
#TODO Add each element to the password variable
#TODO Print the password using an f-string or just by using a print() statement


#Hard Level - Order of characters randomized:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P

#TODO Create an empty list named "characters" to store the characters of the password
#TODO Repeat the same process with choosing a random element from the lists and add it to the list
#TODO Use the shuffle() function to shuffle the characters in the list and then print out the password