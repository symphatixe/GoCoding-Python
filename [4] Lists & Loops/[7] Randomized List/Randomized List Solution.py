# Starter Code
import random
num = int(input("How many numbers do you want inside the list?\n"))

list_a = []
total = 0

# Write your code below!
for _ in range(num):
    list.append(random.randint(0, 9))

for num in list_a:
    total += num


print(f"Randomized list {list_a}, total of numbers: {total}")