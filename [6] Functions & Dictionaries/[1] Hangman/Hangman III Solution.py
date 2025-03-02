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
word_list = ['baboon', 'books', 'bucket', 'coming', 'camel', 'sunshine']


# Write your code below!
game_end = False
lives = 7

choice = random.choice(word_list).lower()


display = []
for letter in choice:
    display += "_"


while not game_end:

  print(f"The word to guess is {" ".join(display)}\n")
  guess = input("Guess a letter\n").lower()

  for position in range(len(choice)):
      letter = choice[position]
      if (letter == guess):
          display[position] = guess

  if guess not in choice:
      lives -= 1
      if lives == 0:
          game_end = True
          print(f"You have lost, the word was {choice}")

  print(stages[lives - 1])

  if ("_") not in display:
    game_end = True
    print("Congratulations for guessing the word!!! :D")