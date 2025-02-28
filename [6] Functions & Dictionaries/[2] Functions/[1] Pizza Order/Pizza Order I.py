# Starter Code
print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L \n").lower()
add_pepperoni = input("Do you want pepperoni? Y or N \n").lower()
extra_cheese = input("Do you want extra cheese? Y or N \n").lower()


# Write your code below!
# small is 15, medium is 20, large is 25
# pepperoni is 2 for small, 3 for medium and large
# extra cheese is 1 for all sizes

#TODO Create a function named bill, that takes three parameters of the size, pepperoni, and the cheese
#TODO Understand why we use the global keyword to change variables initialized outside of the function
#TODO Inside the function create a match case for the inputs and use a ternary operator for the
# pepperoni
#TODO Inside the match case use a wildcard to check for invalid input
#TODO Print out the final bill using an f-string

total = 0