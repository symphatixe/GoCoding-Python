# Starter Code
print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L \n").lower()
add_pepperoni = input("Do you want pepperoni? Y or N \n").lower()
extra_cheese = input("Do you want extra cheese? Y or N \n").lower()


# Write your code below!
# small is 15, medium is 20, large is 25
# pepperoni is 2 for small, 3 for medium and large
# cheese is 1 for all sizes


total = 0

# Calculate bill functions
def bill(s, p, c):
    global total
    if (s == "s"):
        total += 15
    elif (s == "m"):
        total += 20
    elif (s == "l"):
        total += 25

    if p == "y":
        if (s == "s"):
            total += 2

        else:
            total += 3

    if (c == "y"):
        total += 1


bill(size, add_pepperoni, extra_cheese)
print(f"Your final bill is: ${total}.")