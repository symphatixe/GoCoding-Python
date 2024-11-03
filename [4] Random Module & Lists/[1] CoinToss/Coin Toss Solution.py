# Starter Code
import random

print("Welcome to the coin toss simulator, enter toss and choose a value in your head. See if your prediction is right!")
choice = input("Heads or tails? \n").lower()


# Write your code below!
if (choice != "heads" and choice != "tails"):
    print("Not an applicable input.")
    exit()


toss = random.randint(0, 1)
tossChoice = "tails" if toss == 0 else "heads"


match (toss, choice):
    case (0, "tails"):
        print("You chose tails, congratulations on guessing correctly!")
    case (1, "heads"):
        print("You chose heads, congratulations on guessing correctly!")
    case _:
        print(f"Your prediction was not correct, try again. You picked {choice} and the coin was {tossChoice}.")
