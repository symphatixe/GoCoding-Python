# Starter Code
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
            'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

operation = input("Enter 'encode' to encrypt the text or 'decode' to find out the text!\n").lower()
text = input("Enter your text\n").lower()
shift = int(input("Enter the number of characters shifted\n"))

# Write your code below

#TODO Create a function called encrypt that takes text and shift as parameters
#TODO Inside the encrypt function shift each letter of the text using the parameter
"""
Example:
    text = "hello"
    shift = 3

    encoded text = "khoor"
"""

#TODO Create a function called decrypt that will decode the encoded text
#TODO Inside the decrypt function shift every letter back to get the original text
"""
Example:
    text = "khoor"
    shift = 3

    encoded text = "hello"
"""

#TODO Create a match case to detect what operation the user wants and call the appropriate functions


def encrypt(text, shift):
    encoded_text = ""

    for letter in text:
        position = alphabet.index(letter)
        new_position = position + shift

        new_letter = alphabet[new_position]
        encoded_text += new_letter

    print(f"Your original text is {text}")
    print(f"Your encoded text is {encoded_text}")




def decrypt(encoded_text, shift):
    translated_text = ""

    for letter in encoded_text:
        position = alphabet.index(letter)
        new_position = position - shift

        new_letter = alphabet[new_position]
        translated_text += new_letter

    print(f"Your encoded text is {encoded_text}")
    print(f"Your original text is {translated_text}")

match operation:
    case "encode":
        encrypt(text=text, shift=shift)
    case "decode":
        decrypt(encoded_text=text, shift=shift)
    case _:
        print("Error, your input is not understandable")