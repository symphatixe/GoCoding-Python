# Starter Code
age = input("What is your current age? \n")


# Write your code below


calculated_age = 90 - int(age)

months = calculated_age * 12
weeks = calculated_age * 52
days = calculated_age * 365

print(f"You have {days} days, {weeks} weeks, and {months} months left.")
