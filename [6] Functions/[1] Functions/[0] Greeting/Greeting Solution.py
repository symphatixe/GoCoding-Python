# Write your code below!

def greet():
    print("Hello there!")
    print("I am talking to your through the function!")

def greet_name(name):
    print(f"Hey look at that, hello {name}")


greet()
print("\n")

name = input("Enter your name\n").lower()
greet_name(name)