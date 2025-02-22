# Starter Code
print("Welcome to the ArgoPrep Rollercoaster. \n")

height = int(input("What is your height? \n"))
total = 0
photoChoice = False

# Write your code below!
if (height >= 120):
    print("You can ride the ArgoPrep Rollercoaster. \n")

    age = int(input("What is your age? \n"))

    if age < 12:
        total += 5
        print(f"Child tickets are $5. Ticket amount added to bill. Total is now {total}\n")

    elif age <= 18:
        total += 7
        print(f"Youth tickets are $7. Ticket amount added to bill. Total is now {total}\n")

    else:
        total += 12
        print(f"Adult tickets are $12. Ticket amount added to bill. Total is now {total}\n")


    photo = input("Would you like a photo? Please enter y or n. \n").lower()

    if (photo == "y"):
        total += 3
        photoChoice = True
        print(f"You have added the photo package. Total is now {total}")

    elif (photo == "n"):
        print(f"Photo package not chosen. Total is still {total}")

    else:
        print("Not an applicable input.")
        exit()


    if (photoChoice): print(f"\nHello, your total is ${total} and includes a photo.")

    else:
        print(f"\nHello, your total is {total} and does not include a photo.")

else:
    print("You are too short to ride the rollercoaster")