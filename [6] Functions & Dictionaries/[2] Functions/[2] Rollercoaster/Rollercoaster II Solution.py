# Starter Code
print("Welcome to the ArgoPrep Rollercoaster. \n")

height = int(input("What is your height? \n"))
total = 0
photoChoice = False
people = []

# Write your code below!
def ticket():
    global total


    while True:
        age = int(input("What is the ages of everyone as a list, separated by commas? \n"))
        people.append(age)

        for age in people:
            match age:
                case _ if age < 12:
                    total += 5
                    print(f"Child tickets are $5. Ticket amount added to bill. Total is now {total}\n")
                case _ if age <= 18:
                    total += 7
                    print(f"Youth tickets are $7. Ticket amount added to bill. Total is now {total}\n")
                case _:
                    total += 12
                    print(f"Adult tickets are $12. Ticket amount added to bill. Total is now {total}\n")


        entry = input("Do you want to buy more tickets?\n").lower()
        if entry == "yes": continue
        elif entry == "no": break
        else:
            print("Unknown entry")
            break


def photo():
    global total
    global photoChoice
    global people

    response = input("Would you like a photo? Please enter y or n. \n").lower()

    for _ in people:
        match response:
            case "y":
                total += 3
                print(f"You have added the photo package. Total is now {total}")
            case "n":
                print(f"Photo package not chosen. Total is still {total}")
            case _:
                print("Not an applicable input.")
                exit()


def bill():
    print(f"\nHello, your total is ${total}")


match height:
    case _ if height >= 120:
        print("You can ride the ArgoPrep Rollercoaster. \n")
        ticket()
        photo()
        bill()
    case _:
        print("You are too short, cannot ride the rollercoaster")
