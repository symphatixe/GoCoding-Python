# Starter Code
print("Welcome to the Fizz Buzz game, enter a number to test which one it is!")
num = int(input("Enter a number\n"))


# Write your code below!
if (num % 3 == 0):
    if (num % 5 == 0):
        print(f"{num} entered, it is FizzBuzz!")
    else:
        print(f"{num} entered, it is Fizz!")

elif (num % 5 == 0):
    print(f"{num} entered, it is Buzz!")

else:
    print(f"{num} entered, neither category!")