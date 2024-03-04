# Starter Code
year = int(input("Which year do you want to check? \n"))


# Write your code below!
leap1 = year % 4 == 0
leap2 = year % 100 == 0
leap3 = year % 400 == 0

if not leap1:
    print("Not leap year.")
elif leap1 and not leap2:
    print("Leap year.")
elif leap1 and not leap2 and not leap3:
    print("Not leap year.")
else:
    print("Leap year.")