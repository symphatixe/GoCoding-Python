# Starter Code
grades = [90, 60, 90, 40, 50, 100, 70, 40]


# Write your code below!
print("Welcome to the GPA Calculator, let's see if adjusting the grades will help your GPA.")
print(f"Current Grades: {grades}")

total = grades[0] + grades[1] + grades[2] + grades[3] + grades[4] + grades[5] + grades[6] + grades[7]
average = round(float(total) / 8, 2)

print(f"Current Average: {average}\n\n")


"""
You took a test and got another 100 on it, 2nd test grade got dropped, last grade did not count since it was a practice exam, insert a new 3rd test grade
(demonstrate the difference between remove and pop)
"""

# insert() & append() example (also make the recalculation using the last index value)
grades.insert(2, 85)
grades.append(100)
print(f"New Grades: {grades}")

# remove() example
grades.remove(40)
print(f"Remove Grades: {grades}")


"""
explain that you can also input indexes into pop and change the situation to say the first 40 was a practice exam just to showcase the removal
"""

# pop() example
grades.pop(1)
print(f"Pop Grades: {grades}\n")


total = grades[0] + grades[1] + grades[2] + grades[3] + grades[4] + grades[5] + grades[6] + grades[7]
average = round(float(total)/ 8, 2)

print(f"Final Grades: {grades}")
print(f"Final Average: {average}")