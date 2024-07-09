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
        print(f"Child tickets are $5. Ticket amount added to bill. Total is now {total}\n")
        total += 5
        
    elif age <= 18:
        print(f"Youth tickets are $7. Ticket amount added to bill. Total is now {total}\n")
        total += 7
        
    elif age > 18:
        print(f"Adult tickets are $12. Ticket amount added to bill. Total is now {total}\n")
        total += 12
    
    else:
        print("Not an applicable input")
        exit()
        
    photo = input("Would you like a photo? Please enter y or n. \n").lower()
    
    if (photo == "y"):
        print(f"You have added the photo package. Total is now {total}")
        photoChoice = True
        total += 3
        
    elif (photo == "n"):
        print(f"Photo package not chosen. Total is still {total}")
        
    else:
        print("Not an applicable input.")
        exit()

    
    if (photoChoice):
        print(f"\nHello, your total is ${total} and includes a photo.")
    
    else:
        print(f"\nHello, your total is {total} and does not include a photo.")    
    
elif (height < 120):
    print("You are too short, cannot ride the rollercoaster")
    
else:
    print("Not an applicable input.")
    exit()
