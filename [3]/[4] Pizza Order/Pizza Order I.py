# 🚨 Don't change the code below 👇
print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L \n")
add_pepperoni = input("Do you want pepperoni? Y or N \n")
extra_cheese = input("Do you want extra cheese? Y or N \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
total = 0

# Calculate bill functions
if (size == "S"):
    total += 15
elif (size == "M"):
    total += 20
elif (size == "L"):
    total += 25

if (add_pepperoni == "Y" and size == "S"):
    total += 2
elif (add_pepperoni == "Y" and (size == "M" or size == "L")):
    total += 3

if (extra_cheese == "Y"):
    total += 1

# End of code
print(f"Your final bill is: ${total}.")