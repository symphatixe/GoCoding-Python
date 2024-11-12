# Starter Code
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

password = ""


# Write your code below!

def generate_easy_password(nr_letters, nr_symbols, nr_numbers):
    global password
    password = []

    for _ in range(nr_letters):
        password.append(random.choice(letters))
    for _ in range(nr_symbols):
        password.append(random.choice(symbols))
    for _ in range(nr_numbers):
        password.append(random.choice(numbers))

    password = ' '.join(password)

def generate_hard_password(nr_letters, nr_symbols, nr_numbers):
    global password
    characters = []

    for _ in range(nr_letters):
        characters.append(random.choice(letters))
    for _ in range(nr_symbols):
        characters.append(random.choice(symbols))
    for _ in range(nr_numbers):
        characters.append(random.choice(numbers))

    random.shuffle(characters)
    password = ''.join(characters)


def main():
    print("Welcome to the PyPassword Generator!")
    nr_letters= int(input("How many letters would you like in your password?\n"))
    nr_symbols = int(input("How many symbols would you like?\n"))
    nr_numbers = int(input("How many numbers would you like?\n"))

    difficulty = input("Easy password or hard password?\n").lower()

    if difficulty == "easy":
        generate_easy_password(nr_letters, nr_symbols, nr_numbers)
        print(f"Easy Password: {password}")
    elif difficulty == "hard":
        generate_hard_password(nr_letters, nr_symbols, nr_numbers)
        print(f"Hard Password: {password}")
    else:
        print("Invalid choice, run again.")


main()