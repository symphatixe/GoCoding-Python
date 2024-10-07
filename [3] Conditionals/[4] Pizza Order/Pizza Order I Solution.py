# Starter Code
print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L \n")


# Write your code below!
# small is $15, medium is $20, large is $25
# pepperoni is $2 for small, $3 for medium and large
# cheese is $1 for all sizes


total = 0


if (size.lower() == "s"):
    total += 15
    print(f"You have ordered a small pizza. Your total now is ${total} \n")
elif (size.lower() == "m"):
    total += 20
    print(f"You have ordered a medium pizza. Your total now is ${total} \n")
elif (size.lower() == "l"):
    total += 25
    print(f"You have ordered a large pizza. Your total now is ${total} \n")


add_pepperoni = input("Do you want pepperoni? Y or N \n")

if (add_pepperoni.lower() == "y" and size.lower() == "s"):
    total += 2
elif (add_pepperoni.lower() == "y" and (size.lower() == "m" or size.lower() == "l")):
    total += 3
else:
    print(f"You have chosen to not add pepperoni. Your total is still {total}")


extra_cheese = input("Do you want extra cheese? Y or N \n")

if (extra_cheese.lower() == "y"):
    total += 1
else:
    print(f"You have chosen to not add extra cheese. Your total is still {total}")


print(f"Your final bill is: ${total}.")