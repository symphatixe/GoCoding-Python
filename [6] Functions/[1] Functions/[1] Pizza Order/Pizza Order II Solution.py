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
def size_bill(response):
    global total
    if (response == "S"):
        total += 15
    elif (response == "M"):
        total += 20
    elif (response == "L"):
        total += 25

def pepperoni_bill(response):
    global total
    if response == "Y":
        if (size == "S"):
            total += 2

        else:
            total += 3

def cheese_bill(response):
    global total
    if (response == "Y"):
        total += 1


size_bill(size)
pepperoni_bill(add_pepperoni)
cheese_bill(extra_cheese)
print(f"Your final bill is: ${total}.")