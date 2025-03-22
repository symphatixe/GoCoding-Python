# Starter Code
import random

print("Welcome to Hangman")
word_list = ["baboon", "books", "bucket", "coming", "camel", "sunshine"]


# Write your code below!
word = random.word(word_list).lower()

display = []
for _ in word:
    display.append("_")
print(display)

guess = input("Guess a letter\n").lower()

for position in range(len(word)):
    letter = word[position]
    if (letter == guess):
        display[position] = guess

print(display)