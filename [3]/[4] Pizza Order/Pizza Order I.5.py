# Starter Code
print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L \n")
add_pepperoni = input("Do you want pepperoni? Y or N \n")
extra_cheese = input("Do you want extra cheese? Y or N \n")


# Write your code below!
total = 0

# Calculate bill functions
if (size == "S"):
    total += 15
elif (size == "M"):
    total += 20
elif (size == "L"):
    total += 25

if add_pepperoni == "Y":
    if (size == "S"):
        total += 2

    else:
        total += 3

if (extra_cheese == "Y"):
    total += 1


print(f"Your final bill is: ${total}.")