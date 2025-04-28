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
                return True
            else:
                return False
        else:
            return True
    else:
        return False


# Write your code below

def days_in_month(year, month):
    if month > 12 or month < 1: return "Invalid month number"

    if is_leap(year) and month == 2:
        return "There are 29 days in February, because it is a leap year!"
    return f"There are {month_days[month][1]} days in {month_days[month][0]}."

print(days_in_month(year=year, month=month))