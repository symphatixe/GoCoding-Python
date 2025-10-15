# Starter Code
print("Welcome to the Python Simple Calculator!")
num1 = float(input("Enter a number to work with! \n"))
num2 = float(input("Enter a second number to work with! \n"))

operation = int(input("Choose from the menu options below:\n" +
                  "1. Addition\n" +
                  "2. Subtraction\n" +
                  "3. Multiplication\n" +
                  "4. Division\n"))

# Write your code below


match operation:
    case 1:
        result = num1 + num2
        print(f"The result of adding {num1} and {num2} is: {result}")

    case 2:
        result = num1 - num2
        print(f"The result of subtracting {num2} from {num1} is: {result}")

    case 3:
        result = num1 * num2
        print(f"The result of multiplying {num1} and {num2} is: {result}")

    case 4:
        if num2 == 0:
            print("Error: Cannot divide by zero.")

        else:
            result = num1 / num2
            print(f"The result of dividing {num1} by {num2} is: {result}")

    case _:
        print("Invalid choice. Please enter a number between 1 and 4.")