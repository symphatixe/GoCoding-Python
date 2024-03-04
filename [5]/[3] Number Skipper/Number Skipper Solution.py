print("Welcome to the number skipper")
num = int(input("Pick a number to skip :)\n"))

for number in range(0, 11):
    if (number == num):
        continue
    else:
        print(number)