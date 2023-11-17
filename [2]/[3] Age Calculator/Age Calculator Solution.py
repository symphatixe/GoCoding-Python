# 🚨 Don't change the code below 👇
age = input("What is your current age? ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
calculated_age = 90 - int(age)

months = calculated_age * 12
weeks = calculated_age * 52
days = calculated_age * 365

print(f"You have {days} days, {weeks} weeks, and {months} months left.")