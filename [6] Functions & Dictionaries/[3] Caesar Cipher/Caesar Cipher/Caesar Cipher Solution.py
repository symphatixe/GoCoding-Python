# Starter Code
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
from art import logo


# Write your code below

#TODO Create a function called caesar that will combine both encode and decode into one
#TODO Using a for loop we will determine what shift to apply depending on the operation
# Example: If operation is encode + shift, decode is - shift
#TODO Print the completed text using an f-string


def caesar(text, shift, operation):
    completed_text = ""

    if operation == "decode":
        shift *= -1

    for letter in text:
        if letter in alphabet:
            position = alphabet.index(letter)
            new_position = position + shift
            completed_text += alphabet[new_position]
        else:
            completed_text += letter

    print(f"Your completed {operation} operation returned {completed_text}")


while True:
    operation = input("Enter 'encode' to encrypt the text or 'decode' to find out the text!\n").lower()
    text = input("Enter the text to encode\n").lower()
    shift = int(input("Enter the number of characters to shift\n")) % 26

    caesar(operation=operation, text=text, shift=shift)

    selection = input("Would you like to go again? Type 'yes' or 'no'.\n").lower()
    match selection:
        case "no":
            print("Operation terminated")
            break