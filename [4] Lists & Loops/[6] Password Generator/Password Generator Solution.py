# Starter Code
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input("How many symbols would you like in your password?\n"))
nr_numbers = int(input("How many numbers would you like in your password?\n"))

difficulty = input("Easy password or hard password?\n").lower()
password = ""


# Write your code below!

match difficulty:

#Easy Level - Order not randomized:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91
    case "easy":
        for _ in range(nr_letters):
            password += random.choice(letters)
        for _ in range(nr_symbols):
            password += random.choice(symbols)
        for _ in range(nr_numbers):
            password += random.choice(numbers)

        print("Easy password: " + password)


#Hard Level - Order of characters randomized:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P
    case "hard":
        characters = []

        for _ in range(nr_letters):
            characters.append(random.choice(letters))
        for _ in range(nr_symbols):
            characters.append(random.choice(symbols))
        for _ in range(nr_numbers):
            characters.append(random.choice(numbers))

        random.shuffle(characters)
        for char in characters:
            password += char

        print("Hard password: " + password)

    case _:
        print("Invalid choice, try again")