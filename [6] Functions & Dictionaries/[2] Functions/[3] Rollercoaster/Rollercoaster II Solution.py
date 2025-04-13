# Starter Code
print("Welcome to the GoCoding Rollercoaster. \n")

user_response = input("Do you want to run the ticket program?\n").lower()
total = 0
photoChoice = False
people = []

# Write your code below!
def tickets():
    global total
    global people

    while True:
        ages = input("What is the age of everyone as a list, separated by commas? \n")
        people_ages = ages.split(",")

        for age in people_ages:
            match age:
                case _ if int(age) < 12:
                    total += 5
                    print(f"Child tickets are $5. Ticket amount added to bill. Total is now ${total}\n")
                case _ if int(age) <= 18:
                    total += 7
                    print(f"Youth tickets are $7. Ticket amount added to bill. Total is now ${total}\n")
                case _:
                    total += 12
                    print(f"Adult tickets are $12. Ticket amount added to bill. Total is now ${total}\n")


        people.extend(people_ages)
        entry = input("Do you want to buy more tickets?\n").lower()
        if entry == "yes": continue
        elif entry == "no": break
        else:
            print("Unknown entry")
            break


def photo(people_list):
    global total
    global photoChoice

    for _ in people_list:
        response = input("Would you like a photo? Please enter y or n. \n").lower()

        match response:
            case "y":
                total += 3
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
        print("Running program!\n")

        tickets()
        photo(people)
        bill()
    case "no":
        print("You chose to not run the rollercoaster program.")
    case _:
        print("Unknown response, terminating!")
