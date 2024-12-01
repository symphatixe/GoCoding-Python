# Starter Code
import math

print("""
      You are painting a wall, each can of paint covers 5 square meters.
      Given a width and height, determine the maximum number of meters that can be covered.
      """)

height = float(input("Enter the height of the wall\n"))
width = float(input("Enter the width of the wall\n"))
coverage = 5


# Write your code below!

def paint_calc(height, width, coverage):
    area = height * width
    cans = math.ceil(area / coverage)

    print(f"You need {cans} cans of paint for the wall.")


paint_calc(height=height, width=width, coverage=coverage)