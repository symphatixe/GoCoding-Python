# Starter Code
month_days = {
    1: ["January", 31],
    2: ["February", 28],
    3: ["March", 31],
    4: ["April", 30],
    5: ["May", 31],
    6: ["June", 30],
    7: ["July", 31],
    8: ["August", 31],
    9: ["September", 30],
    10: ["October", 31],
    11: ["November", 30],
    12: ["December", 31]
}

year = int(input("Enter a year:\n"))
month = int(input("Enter a month:\n"))

def is_leap(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                print("Leap year.")
            else:
                print("Not leap year.")
        else:
            print("Leap year.")
    else:
        print("Not leap year.")


# Write your code below

#TODO Complete the tasks below!
"""
» Adjust the is_leap() function to return True or False
» Create a function named days_in_month() that will return the number of days in a month
    › Catch any errors with invalid month numbers
    › Check if the year is a leap year using is_leap() and month is 2 (February)
    › If the year is a leap year, return 29 for February only
    › Otherwise return the days in a given month using the dictionary
    › NOTE Please keep in mind the month number has a list with the name and amount of days
» HINT: February has 29 days in a leap year, other months do not change.
» Print out the days in that given month by calling the function
"""