import random

print("Welcome to Hangman")
game_end = False

word_list = ['baboon', 'books', 'bucket', 'coming', 'camel', 'sunshine']
choice = random.choice(word_list).lower()


display = []
for letter in choice:
    display += "_"
print(display)


while not game_end:

    guess = input("Guess a letter\n")

    for position in range(len(choice)):
        letter = choice[position]
        if (letter == guess):
            display[position] = guess
            
    print(display)
    
    if ("_") not in display:
        game_end = True
        print("You have won")