# Starter Code
print("Welcome to the GoCoding Rollercoaster. \n")

user_response = input("Do you want to run the rollercoaster program?\n").lower()
total = 0
photoChoice = False

# Write your code below!


#TODO Create a match case for whether the person wants to run the rollercoaster ticket program
"""
TODO Create a function with match case to check the age for the ticket price
TODO Get the amount of the tickets that want to be purchased
    - child tickets are age less than 12, $5
    - youth tickets are age less than or equal to 18, $7
    - adult tickets are anything else greater than 18, $12
"""
#TODO Make sure the variables are set to lower() globally
#TODO Create a function to check the user's choice for a photo
#TODO Using match case change the variable, update the total and print it out
#TODO Create a conditional to print out whether they chose a photo or not and the proper total
#TODO Create simple exceptions using else and exit() to stop the program running on invalid input
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

def photo(people):
    global total
    global photoChoice

    photo = input("")
    match photo:
        case "yes" | "y":
            total += (3 * people)
            photoChoice = True
            print(f"You have added the photo package. Total is now ${total}")
        case "n":
            print(f"Photo package not chosen. Total is still ${total}")
        case _:
            print("Not an applicable input.")
            exit()

match user_response:
    case "yes":
        print("You can ride the GoCoding Rollercoaster. \n")
        
        people = int(input("How many people want tickets?\n"))
        tickets(people)
    case "no":
        print("Okay, exiting")
    case _:
        print("Unknown command")