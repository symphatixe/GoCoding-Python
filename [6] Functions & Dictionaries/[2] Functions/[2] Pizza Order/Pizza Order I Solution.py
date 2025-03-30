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
def bill(s, p, c):
    global total

    match s:
        case "s": total += 15
        case "m": total += 20
        case "l": total += 25
        case _:
            print("Invalid input, no size like that exists")
            exit()

    match p:
        case "y": total += 2 if size == "s" else 3
        case "n": print("No pepperoni added.")
        case _:
            print("What did you enter besides yes or no?")
            exit()

    match c:
        case "y": total += 1
        case "n": print("No extra cheeses added.")
        case _:
            print("What did you enter besides yes or no?")
            exit()

    print(f"Your final bill is: ${total}.")


bill(size, add_pepperoni, extra_cheese)