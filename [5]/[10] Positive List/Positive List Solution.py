# Starter Code
import random

list = []
list2 = []


# Write your code below!
for num in range(35):
    number = random.randint(-20, 20)
    if (number >= 0):
        list.append(number)
        list2.append(number)
    else:
        list.append(number)
        

print("Full list: " + str(list))
print("Positive list: " + str(list2))