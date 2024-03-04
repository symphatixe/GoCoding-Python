import random

print("Welcome to the hangman game")

word_list = ['baboon', 'books', 'bucket', 'coming', 'camel', 'sunshine']
choice = random.choice(word_list).lower()

guess = input("Guess a letter")

for letter in choice:
    if (letter == guess):
        print("Correct!")
    else:
        print("Incorrect")
        
        