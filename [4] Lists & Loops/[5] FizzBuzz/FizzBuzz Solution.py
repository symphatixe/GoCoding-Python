# Starter Code
print("Welcome to the Fizz Buzz game, enter a number to test which one it is!")
num = int(input("Enter a number\n"))


# Write your code below!
match num:
    case _ if num % 3 == 0 and num % 5 == 0:
        print(f"{num} entered, it is FizzBuzz!")
    case _ if num % 3 == 0:
        print(f"{num} entered, it is Fizz!")
    case _ if num % 5 == 0:
        print(f"{num} entered, it is Buzz!")
    case _:
        print(f"{num} is not applicable to this program :)")