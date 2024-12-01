# Starter Code
print("Welcome to the ArgoPrep Rollercoaster. \n")

height = int(input("What is your height? \n"))
total = 0
photoChoice = False

# Write your code below!
def ticket(response):
    global total

    match response:
        case _ if response < 12:
            total += 5
            print(f"Child tickets are $5. Ticket amount added to bill. Total is now {total}\n")
        case _ if response <= 18:
            total += 7
            print(f"Youth tickets are $7. Ticket amount added to bill. Total is now {total}\n")
        case _:
            total += 12
            print(f"Adult tickets are $12. Ticket amount added to bill. Total is now {total}\n")


def photo(response):
    global total
    global photoChoice

    match response:
        case "y":
            total += 3
            photoChoice = True
            print(f"You have added the photo package. Total is now {total}")
        case "n":
            print(f"Photo package not chosen. Total is still {total}")
        case _:
            print("Not an applicable input.")
            exit()


def bill(response):
    print(f"\nHello, your total is ${total} and includes a photo."
          if response
          else f"\nHello, your total is {total} and does not include a photo.")


match height:
    case _ if height >= 120:
        print("You can ride the ArgoPrep Rollercoaster. \n")

        age = int(input("What is your age? \n"))
        ticket(age)

        photoInput = input("Would you like a photo? Please enter y or n. \n").lower()
        photo(photoInput)

        bill(photoChoice)
    case _:
        print("You are too short, cannot ride the rollercoaster")
