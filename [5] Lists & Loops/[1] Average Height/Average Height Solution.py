# Starter Code
student_heights = [180, 124, 165, 173, 189, 169, 146]


# Write your code below!

#NOTE: You should not use the sum() or len() functions in your answer.

total = 0
count = 0
for h in student_heights:
    total += h
    count += 1

print(f"The average is {round(total / count, 2)}")
