import random

name_string = input("Enter the names of everyone, separated by a comma.")
names = name_string.split(", ")

print(names[random.randint(0, len(names) - 1)] + " will pay for dinner today!")