# Starter Code
import random
num1 = int(input("How many numbers do you want inside the first list?\n"))
num2 = int(input("How many numbers do you want inside the second list?\n"))

list_a = []
list_b = []
# Write your code below!

for _ in range(num1):
    list_a.append(random.randint(0, 9))

for _ in range(num2):
    list_b.append(random.randint(0, 9))

print(f"List 1: {list_a}")
print(f"List 2: {list_b}")

list_c = list_a + list_b
print(f"List 3: {list_c}")

list_c.sort()
print(f"List 3 Sorted: {list_c}")