# Starter Code
import random

list1 = []
list2 = []


# Write your code below!
for num in range(35):
    number = random.randint(-20, 20)
    list1.append(number)
    if (number >= 0):
        list2.append(number)

print(f"Full list: {list1}")
print(f"Positive list: {list2}")
