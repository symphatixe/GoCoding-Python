# Starter Code
print("Welcome to the number skipper!")
num = int(input("Pick a number to skip :)\n"))


# Write your code below!

for number in range(1, 11):
    if number == num:
        continue
    print(number)