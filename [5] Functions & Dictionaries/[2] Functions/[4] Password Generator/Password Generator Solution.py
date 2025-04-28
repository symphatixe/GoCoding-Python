# Starter Code
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

password = ""


# Write your code below!

def generate_password(nr_characters, difficulty):
    global password
    characters = []

    for _ in range(nr_characters):

        lists = [letters, numbers, symbols]
        selected_list = random.choice(lists)
        selected_character = random.choice(selected_list)

        characters.append(selected_character)

    match difficulty:
        case "easy":
            password = ' '.join(characters)
            print(f"Easy Password: {password}")
        case "hard":
            random.shuffle(characters)
            password = ''.join(characters)
            print(f"Hard Password: {password}")


def main():
    print("Welcome to the PyPassword Generator!")
    nr_characters= int(input("How many characters would you like in your password?\n"))
    difficulty = input("Easy password or hard password?\n").lower()

    if difficulty != "easy" and difficulty != "hard":
        print("Invalid input")
        exit()

    generate_password(nr_characters=nr_characters, difficulty=difficulty)


main()