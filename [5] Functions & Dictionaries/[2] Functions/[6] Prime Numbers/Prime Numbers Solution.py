# Starter Code
print("Welcome to the prime number checker!")

num = int(input("Enter a number to check if it is prime.\n"))


# Write your code below!

def prime_check(number):
    prime = True

    for i in range(2, number):
        if number % i == 0:
            prime = False

    print(f"{number} is prime."
          if prime
          else f"{number} is not prime.")

prime_check(number=num)