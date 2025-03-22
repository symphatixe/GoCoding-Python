# Write your code below

def format_name(f_name, l_name):
    if f_name == "" or l_name == "":
        return "No names were provided"

    formatted_name = f_name.title() + " " + l_name.title()
    return f"Result: {formatted_name}"

print(format_name(input("What is your first name?\n"), input("What is your last name?\n")))