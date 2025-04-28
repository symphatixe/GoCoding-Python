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
choice = random.choice(words).lower()


display = []
for letter in choice:
    display += "_"
# This list is used to store the guessed letters
guesses = []


while not game_end:
    print(f"The word to guess is {' '.join(display)}\n")
    guess = input("Guess a letter\n")

    if guess not in guesses:
        # TODO Add the letter to the guesses list
        # TODO Print out the list of guessed letters

        # TODO Add a conditional to check for the letter already existing inside the word
        # TODO Take away one life and print out the list of guessed letters again
        # TODO Inform the user that they have entered the wrong letter using a condition and print the amount of lives


        for position in range(len(choice)):
            letter = choice[position]
            if (guess == letter):
                display[position] = letter
    else:
        # TODO Print out the list of guessed letters
        print(f"You have already tried {letter}, you have {lives} lives left.")

    print(stages[lives - 1])

    if lives == 0:
        game_end = True
        print(f"You have lost, the word was {choice}")

    if ("_") not in display:
        game_end = True
        print(f"{' '.join(display)}")
        print(f"You have won, the word is {choice}!")