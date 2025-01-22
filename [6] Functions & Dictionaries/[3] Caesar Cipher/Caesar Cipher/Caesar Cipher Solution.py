# Starter Code
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
from art import logo


# Write your code below
print(logo)

def caesar(text, shift, operation):
    completed_text = ""

    if operation == "decode":
        shift *= -1

    for letter in text:
        if letter in alphabet:
            position = alphabet.index(letter)
            completed_text += alphabet[(position + shift) % 26]
        else:
            completed_text += letter

    print(f"Your completed {operation} operation returned {completed_text}")


while True:
    operation = input("Enter 'encode' to encrypt the text or 'decode' to find out the text!\n").lower()
    text = input("Enter the text to encode or decode\n").lower()
    shift = int(input("Enter the number of characters to shift\n")) % 26


    if operation != "encode" and operation != "decode":
        print("Invalid")

    caesar(operation=operation, text=text, shift=shift)

    selection = input("Would you like to go again? Type 'yes' or 'no'.\n").lower()
    match selection:
        case "yes":
            continue
        case "no":
            print("Operation terminated.")
            exit()
        case _:
            print("Invalid input.")
            exit()
