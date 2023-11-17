# 🚨 Don't change the code below 👇
print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
total = 0

# Calculate bill functions
def pizza_bill(response):
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

# End of code
pizza_bill(size)
pepperoni_bill(add_pepperoni)
cheese_bill(extra_cheese)
print(f"Your final bill is: ${total}.")