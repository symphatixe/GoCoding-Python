# Starter Code
import random

list = []
list2 = []


# Write your code below!
for num in range(35):
    number = random.randint(-20, 20)
    list.append(number)
    if (number >= 0):
        list2.append(number)

print(f"Full list: {list}")
print(f"Positive list: {list2}")
