# Starter Code
student_scores = [78, 65, 89, 86, 55, 91, 64, 89]


# Write your code below!

#NOTE: You are not allowed to use the max() or min() functions.

max = 0

for score in student_scores:
    if (score > max): max = score

print(f"The highest student score is {max}")