# Write your code below!

#TODO Create a function called greet() that will print a greeting
#TODO Create another function called greet() that takes a parameter of a name and prints that

def greet():
    print("hello vadim")

def greet_name(name: str, age: int):
    print(f"My name is {name}")
    print(age + 5)
    print("This is how I use a function with a parameter!")

greet()

greet_name(age=5, name="vadim")

fruit: str = ""