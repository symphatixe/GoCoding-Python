# Starter Code
import random

stages = [
'''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''',
'''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''',
'''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', 
'''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========
''',
'''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''',
'''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''',
'''
  +---+
  |   |
      |
      |
      |
      |
=========
''']



print("Welcome to Hangman")
word_list = ["baboon", "books", "bucket", "coming", "camel", "sunshine"]


# Write your code below!

#TODO Create two variables
# - Boolean to store whether the game has ended
# - How many lives are left (7 lives)
#TODO Create a while loop that will run while game has not ended
#TODO Inside the while loop we will display the word as underscores to guess
#TODO The player can guess a letter and will take away lives if the guess is incorrect
#TODO If there are no underscores left then the player has won.

lives = 7
game_end = False

word = random.choice(word_list).lower()
display = []
for _ in word:
    display += "_"

while not game_end:

  print(f"The word to guess is {" ".join(display)}\n")
  guess = input("Guess a letter\n").lower()

  for position in range(len(word)):
      letter = word[position]
      if (letter == guess):
          display[position] = guess