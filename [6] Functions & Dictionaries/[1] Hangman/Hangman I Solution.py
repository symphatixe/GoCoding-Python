# Starter Code
import random

print("Welcome to Hangman")
word_list = ["baboon", "books", "bucket", "coming", "camel", "sunshine"]


# Write your code below!
choice = random.choice(word_list).lower()

guess = input("Guess a letter!\n").lower()

for letter in choice:
    print("Correct"
        if letter == guess
        else "Incorrect")