# Starter Code
import random

print("Welcome to Hangman")
word_list = ['baboon', 'books', 'bucket', 'coming', 'camel', 'sunshine']


# Write your code below!
choice = random.choice(word_list).lower()

guess = input("Guess a letter!\n")

for letter in choice:
    if (letter == guess):
        print("Correct!")
    else:
        print("Incorrect")