# Starter Code
print("Welcome to the Python Simple Calculator!")
num1 = float(input("Enter a number to work with!"))
num2 = float(input("Enter a second number to work with!"))

operation = int(input("Choose from the menu options below:\n" +
                  "1. Addition\n" +
                  "2. Subtraction\n" +
                  "3. Multiplication\n" +
                  "4. Division\n"))

# Write your code below

#TODO Create a match case based off the operation variable to determine what operation the user wants
#TODO Inside the cases create the arithmetic operation and print it using an f-string
#TODO Inside the case for division check for division by 0
#TODO Lastly add a case for handling invalid choices that are not 1 - 4