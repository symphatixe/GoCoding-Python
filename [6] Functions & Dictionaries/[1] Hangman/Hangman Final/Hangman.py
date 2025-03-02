# Starter Code
# TODO Import the files using both just import and using from to import specific variables/functions
import random
import hangman_words as words
# from hangman_words import word_list as words
import hangman_art as art
# from hangman_art import stages


print("Welcome to Hangman")


# Write your code below!
game_end = False
lives = 7

# TODO Import the word list from the hangman_words file, there are two versions using import and the from
choice = random.choice(word_list).lower()


display = []
for letter in choice:
    display += "_"
# This list is used to store the guessed letters
guesses = []


while not game_end:
    print(f"The word to guess is {' '.join(display)}\n")
    guess = input("Guess a letter\n")

    if guess not in guesses:
        # TODO Add the incorrect letter to the guesses list
        # TODO Print out the list of guessed letters
        # TODO Add a conditional to check for the guess already existing inside the word
        # TODO Inform the user that they have entered the wrong letter using a condition and print the amount of lives
        lives -= 1

        for position in range(len(choice)):
            letter = choice[position]
            if (letter == guess):
                display[position] = guess
    else:
        # TODO Print out the list of guessed letters
        print(f"You have already tried {guess}, you have {lives} lives left.")

    print(stages[lives - 1])

    if lives == 0:
        game_end = True
        print(f"You have lost, the word was {choice}")

    if ("_") not in display:
        game_end = True
        print(f"{' '.join(display)}")
        print(f"You have won, the word is {choice}!")