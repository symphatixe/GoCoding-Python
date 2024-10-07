# Starter Code
import random
num = int(input("How many numbers do you want inside the list?\n"))


# Write your code below!
# Insertion at position to be covered
list = []

for _ in range(num):
    list.append(random.randint(0, 9))

print(list)
list.pop()
print(f"{list} after removing the last element")
print(list.pop(0))
print(f"{list} after removing the first element")