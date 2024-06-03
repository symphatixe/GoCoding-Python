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
if (size.lower() == "s"):
    total += 15
elif (size.lower() == "m"):
    total += 20
elif (size.lower() == "l"):
    total += 25

if (add_pepperoni == "Y" and size == "S"):
    total += 2
elif (add_pepperoni == "Y" and (size == "M" or size == "L")):
    total += 3

if (extra_cheese == "Y"):
    total += 1


print(f"Your final bill is: ${total}.")