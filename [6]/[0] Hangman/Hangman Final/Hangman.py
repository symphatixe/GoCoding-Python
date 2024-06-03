# Starter Code
# TODO: import the files using both just import and using from to import specific variables/functions
import random


print("Welcome to Hangman")


# Write your code below!
game_end = False
lives = 7

# TODO: import the word list from the hangman_words file, there are two versions using import and the from
choice = random.choice(word_list).lower()


display = []
for letter in choice:
    display += "_"


while not game_end:
  
    print(f"The word to guess is {' '.join(display)}\n")
    guess = input("Guess a letter\n")
    
    # TODO: add a conditional to check for the guess already exising inside the word

    for position in range(len(choice)):
        letter = choice[position]
        if (letter == guess):
            display[position] = guess
            
            
    # TODO: import the stages from the hangman_art file, there are two versions using import and the from
    print(stages[lives - 1])


    if guess not in choice:
        # TODO: inform the user that they have entered the wrong letter using a condition
        
        lives -= 1
        if lives == 0:
            game_end = True
            print(f"You have lost, the word was {choice}")

    if ("_") not in display:
        game_end = True
        print(f"{' '.join(display)}")
        print(f"You have won, the word is {choice}!")