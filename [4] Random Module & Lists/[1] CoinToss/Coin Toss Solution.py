# Starter Code
import random

print("Welcome to the coin toss simulator, enter toss and choose a value in your head. See if your prediction is right!")
choice = input("Heads or tails? \n").lower()


# Write your code below!
if (choice != "heads" and choice != "tails"):
    print("Not an applicable input.")
    exit()


toss = random.randint(0, 1)
tossChoice = ""
if (toss == 0):
    tossChoice = str("tails")
else:
    tossChoice = str("heads")


if (toss == 0 and choice == "tails"):
    print("You chose tails, congratulations!")
elif (toss == 1 and choice == "heads"):
    print("You chose heads, congratulations!")
else:
    print(f"Your prediction was not correct, try again. You picked {choice} and the coin was {tossChoice}.")
