# Starter Code
import random
import hangman_words as words
# from hangman_words import word_list
import hangman_art as art
# from hangman_art import stages



print("Welcome to Hangman")


# Write your code below!
game_end = False
lives = 7

choice = random.choice(words.word_list).lower()


display = []
for letter in choice:
    display += "_"
guesses = []


while not game_end:
    print(f"The word to guess is {' '.join(display)}\n")
    guess = input("Guess a letter\n")

    if guess not in guesses:
        guesses.append(guess)
        print(f"Guessed letters: {guesses}")

        if guess not in choice:
            lives -= 1
            print(f"You have guessed {guess}, that is not correct. You have {lives} lives left.")
        else:
            for position in range(len(choice)):
                letter = choice[position]
                if (letter == guess):
                    display[position] = guess
    else:
        print(f"Guessed letters: {guesses}")
        print(f"You have already tried {guess}, you have {lives} lives left.")

    print(art.stages[lives - 1])

    if lives == 0:
        game_end = True
        print(f"You have lost, the word was {choice}.")

    if ("_") not in display:
        game_end = True
        print(f"{' '.join(display)}")
        print(f"You have won, the word is {choice}!")