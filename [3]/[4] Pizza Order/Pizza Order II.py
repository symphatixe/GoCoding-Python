# Starter Code
print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L \n")
add_pepperoni = input("Do you want pepperoni? Y or N \n")
extra_cheese = input("Do you want extra cheese? Y or N \n")


# Write your code below!
# small is 15, medium is 20, large is 25
# pepperoni is 2 for small, 3 for medium and large
# cheese is 1 for all sizes


total = 0

# Calculate bill functions
def bill(size, pepperoni, cheese):
    global total
    if (size == "S"):
        total += 15
    elif (size == "M"):
        total += 20
    elif (size == "L"):
        total += 25

    if pepperoni == "Y":
        if (size == "S"):
            total += 2

        else:
            total += 3

    if (cheese == "Y"):
        total += 1


bill(size, add_pepperoni, extra_cheese)
print(f"Your final bill is: ${total}.")