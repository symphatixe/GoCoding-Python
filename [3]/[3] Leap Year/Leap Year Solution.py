# Starter Code
year = int(input("Which year do you want to check? \n"))


# Write your code below!
leap1 = year % 4 == 0
leap2 = year % 100 == 0
leap3 = year % 400 == 0

if (not leap1):
    print(f"{year} is not leap year.")
elif (leap1 and not leap2):
    print(f"{year} is a leap year.")
elif (leap1 and not leap2 and not leap3):
    print(f"{year} is not a leap year.")
elif (leap1 and not leap2 and leap3):
    print(f"{year} is a leap year.")
else:
    print("Not an applicable input.")
    exit()