# Starter Code
import random
import hangman_words as words
# from hangman_words import word_list as words
import hangman_art as art
# from hangman_art import stages as art



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
    print(f"Guessed letters {guesses}")

    if guess not in guesses:
        guesses.append(guess)
        lives -= 1
        print(art.stages[lives - 1])
        print(f"You have guessed {guess}, that is not correct. You have {lives} lives left.")

        for position in range(len(choice)):
            letter = choice[position]
            if (letter == guess):
                display[position] = guess
    else:
        print(f"You have already tried {guess}")


    if lives == 0:
        game_end = True
        print(f"You have lost, the word was {choice}.")

    if ("_") not in display:
        game_end = True
        print(f"{' '.join(display)}")
        print(f"You have won, the word is {choice}!")