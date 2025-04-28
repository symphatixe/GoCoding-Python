# Starter Code
print("Welcome to the FizzBuzz looper!")


# Write your code below!
for number in range(101):
    match number:
        case _ if number % 3 == 0 and number % 5 == 0:
            print(f"{number} entered, it is FizzBuzz!")
        case _ if number % 3 == 0:
            print(f"{number} entered, it is Fizz!")
        case _ if number % 5 == 0:
            print(f"{number} entered, it is Buzz!")
        case _:
            print(f"{number} is not applicable to this program :)")