# Starter Code
print("Welcome to add evens!")
total = 0


# Write your code below!


for number in range(0, 101, 2):
    total += number

"""
alternate solution:

for number in range(1, 101):
    if (number % 2 == 0):
        total += number
"""

print(f"Even numbers added up from 1 - 100 is {total}")