# Starter Code
print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L \n").lower()


# Write your code below!
# small is $15, medium is $20, large is $25
# pepperoni is $2 for small, $3 for medium and large
# cheese is $1 for all sizes

total = 0


if (size == "s"):
    total += 15
    print(f"You have ordered a small pizza. Your total now is ${total} \n")
elif (size == "m"):
    total += 20
    print(f"You have ordered a medium pizza. Your total now is ${total} \n")
elif (size == "l"):
    total += 25
    print(f"You have ordered a large pizza. Your total now is ${total} \n")
else:
    print("No applicable size selected.")
    exit()


add_pepperoni = input("Do you want pepperoni? Y or N \n").lower()

if (add_pepperoni == "y"):
    if (size == "s"):
        total += 2
        print(f"You ordered pepperoni for a small pizza. Your total now is ${total} \n")
    else:
        total += 3
        print(f"You ordered pepperoni for a medium or large pizza. Your total now is ${total} \n")
elif (add_pepperoni == "n"):
    print(f"You have chosen to not add pepperoni. Your total is still {total}")
else:
    print("Not an applicable input.")
    exit()


extra_cheese = input("\nDo you want extra cheese? Y or N \n").lower()

if (extra_cheese == "y"):
    total += 1
    print(f"You ordered extra cheese for your pizza. Your total now is ${total} \n")
elif (extra_cheese == "n"):
    print(f"You have chosen to not add pepperoni. Your total is still {total}")
else:
    print("Not an applicable input.")
    exit()


print(f"\nYour final bill is: ${total}.")