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
game_end = False
lives = 6

word_list = ['baboon', 'books', 'bucket', 'coming', 'camel', 'sunshine']
choice = random.choice(word_list).lower()
print(choice)


display = []
for letter in choice:
    display += "_"


while not game_end:

    guess = input("Guess a letter\n")

    for position in range(len(choice)):
        letter = choice[position]
        if (letter == guess):
            display[position] = guess
            
    print(f"{' '.join(display)}\n")
    
    if guess not in choice:
        lives -= 1
        if lives == 0:
            game_end = True
            print("You have lost!")
    
    if ("_") not in display:
        game_end = True
        print(f"{' '.join(display)}")
        print(f"You have won, the word is {choice}!")