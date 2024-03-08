# Starter Code
import random

print("Welcome to the coin toss simulator, enter toss and choose a value in your head. See if your prediction is right!")
choice = input("Heads or tails? \n")


# Write your code below!
toss = random.randint(0, 1)
if (toss == 0):
    toss = str("tails")
else:
    toss = str("heads")

if (toss == 0 and choice.lower() == "tails"):
    print("You chose tails, congratulations!")
elif (toss == 1 and choice.lower() == "heads"):
    print("You chose heads, congratulations!")
else:
    print(f"Your prediction was not correct, try again. You picked {choice} and the coin was {toss}. 0 means tails and 1 is heads.")
