# Starter Code
import random
num1 = int(input("How many numbers do you want inside the first list?\n"))
num2 = int(input("How many numbers do you want inside the second list?\n"))


# Write your code below!

list1 = []
list2 = []

for _ in range(num1):
    list1.append(random.randint(0, 9))
    
for _ in range(num2):
    list2.append(random.randint(0, 9))
    
print("List 1: " + str(list1))
print("List 2: " + str(list2))

list3 = list1 + list2
print("List 3: " + str(list3))

list3.sort()
print("List 3 Sorted: " + str(list3))