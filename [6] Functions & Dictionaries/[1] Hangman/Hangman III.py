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
word_list = []


# Write your code below!

#TODO Create two variables
# - Boolean to store whether the game has ended
# - How many lives are left
#TODO Create a while loop that will run while game has not ended
#TODO Inside the while loop we will display the word as underscores to guess
#TODO The player can guess what 