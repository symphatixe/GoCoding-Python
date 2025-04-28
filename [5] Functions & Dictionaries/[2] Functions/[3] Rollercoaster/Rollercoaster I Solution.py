# Starter Code
print("Welcome to the GoCoding Rollercoaster. \n")

user_response = input("Do you want to run the rollercoaster?\n").lower()
total = 0
photoChoice = False

# Write your code below!
def tickets(people):
    global total

    age = int(input("What is your age? \n"))
    match age:
        case _ if age < 12:
            total += (5 * people)
            print(f"Child tickets are $5. Ticket amount added to bill. Total is now ${total}\n")
        case _ if age <= 18:
            total += (7 * people)
            print(f"Youth tickets are $7. Ticket amount added to bill. Total is now ${total}\n")
        case _:
            total += (12 * people)
            print(f"Adult tickets are $12. Ticket amount added to bill. Total is now ${total}\n")


def photo(response, people):
    global total
    global photoChoice

    match response:
        case "y":
            total += 3 * people
            photoChoice = True
            print(f"You have added the photo package. Total is now ${total}")
        case "n":
            print(f"Photo package not chosen. Total is still ${total}")
        case _:
            print("Not an applicable input.")
            exit()


def bill():
    print(f"\nHello, your total is ${total} and includes photos."
          if photoChoice
          else f"\nHello, your total is ${total} and does not include photos.")



match user_response:
    case "yes":
        print("You can ride the GoCoding Rollercoaster. \n")

        people = int(input("How many people want tickets?\n"))
        tickets(people)

        photoInput = input("Would you like a photo? Please enter y or n. \n").lower()
        photo(photoInput, people)

        bill()
    case "no":
        print("Okay, exiting")
    case _:
        print("Unknown command")
