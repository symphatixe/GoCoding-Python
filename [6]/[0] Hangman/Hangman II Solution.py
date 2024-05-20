# Starter Code
import random

print("Welcome to Hangman")
word_list = ['baboon', 'books', 'bucket', 'coming', 'camel', 'sunshine']


# Write your code below!
choice = random.choice(word_list).lower()

print(choice)

display = []
for letter in choice:
    display += "_"
print(display)

guess = input("Guess a letter\n")

for position in range(len(choice)):
    letter = choice[position]
    if (letter == guess):
        display[position] = guess
        
print(display)