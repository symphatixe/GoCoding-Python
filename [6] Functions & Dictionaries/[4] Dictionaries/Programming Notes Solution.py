# Starter Code

programming_dictionary = {
    "Bug": "Bzzzz bzzbzbzbzbzzbzbz zzzzz",
    "Loop": "The action of doing something over and over again.",
    "Function": "A piece of code that you can easily call over and over again."
}


# Write your code below

programming_dictionary["Casting"] = "Conversion of data types."
programming_dictionary["Bug"] = "An error in a program that prevents the program from running as expected."

for key in programming_dictionary:
    print(f"The concept is {key}, the definition is '{programming_dictionary[key]}'")