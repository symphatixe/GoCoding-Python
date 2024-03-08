# Starter Code
print("Welcome to the ArgoPrep Rollercoaster.\n")

height = int(input("What is your height? "))
total = 0
photo = False


# Write your code below!
if (height >= 120):
    print("You can ride the ArgoPrep Rollercoaster. \n")
    
    age = int(input("What is your age? \n"))
    
    if age < 12:
        print("Child tickets are $5. Ticket amount added to bill.\n")
        total += 5
        
    elif age <= 18:
        print("Youth tickets are $7. Ticket amount added to bill.\n")
        total += 7
        
    else:
        print("Adult tickets are $12. Ticket amount added to bill.\n")
        total += 12
        
        
    photo = input("Would you like a photo? Please enter y or n. \n")
    
    if (photo.lower() == "y"):
        print("You have added the photo package.")
        total += 3
        
    elif (photo.lower() == "n"):
        print("Photo package not chosen.")
        
    else:
        print("Invalid choice, please try again.")

    
    if (photo):
        print(f"\nHello, your total is ${total} and includes a photo.")
    
    else:
        print(f"\nHello, your total is {total} and does not include a photo.")    
    
else:
    print("You are too short, cannot ride")
    
    
