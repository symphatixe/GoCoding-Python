# Starter Code
print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L \n").lower()


# Write your code below!
# small is $15, medium is $20, large is $25
# pepperoni is $2 for small, $3 for medium and large
# extra cheese is $1 for all sizes


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


add_pepperoni = input("Do you want pepperoni? Y or N \n").lower()

if (add_pepperoni == "y" and size == "s"):
    total += 2
elif (add_pepperoni == "y" and (size == "m" or size == "l")):
    total += 3
else:
    print(f"You have chosen to not add pepperoni. Your total is still {total}")


extra_cheese = input("Do you want extra cheese? Y or N \n").lower()

if (extra_cheese == "y"):
    total += 1
else:
    print(f"You have chosen to not add extra cheese. Your total is still {total}")


print(f"Your final bill is: ${total}.")