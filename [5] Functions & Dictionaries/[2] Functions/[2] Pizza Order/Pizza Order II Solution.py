# Starter Code
print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L \n").lower()
add_pepperoni = input("Do you want pepperoni? Y or N \n").lower()
extra_cheese = input("Do you want extra cheese? Y or N \n").lower()


# Write your code below!
# small is 15, medium is 20, large is 25
# pepperoni is 2 for small, 3 for medium and large
# extra cheese is 1 for all sizes


total = 0

# Calculate bill functions
def size_bill(response):
    global total

    match response:
        case "s": total += 15
        case "m": total += 20
        case "l": total += 25
        case _:
            print("Invalid input, no size like that exists")
            exit()

def pepperoni_bill(response):
    global total

    match response:
        case "y": total += 2 if size == "s" else 3
        case "n": print("No pepperoni added.")
        case _:
            print("What did you enter besides yes or no?")
            exit()

def cheese_bill(response):
    global total

    match response:
        case "y": total += 1
        case "n": print("No extra cheese added.")
        case _:
            print("What did you enter besides yes or no?")
            exit()

size_bill(size)
pepperoni_bill(add_pepperoni)
cheese_bill(extra_cheese)
print(f"Your final bill is: ${total}.")