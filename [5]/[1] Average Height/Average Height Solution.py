# 🚨 Don't change the code below 👇
student_heights = [180, 124, 165, 173, 189, 169, 146]
#student_heights = input("Input a list of student heights ").split()
#for n in range(0, len(student_heights)):
#  student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆


#Write your code below this row 👇
# Important You should not use the sum() or len() functions in your answer.
total = 0
count = 0
for h in student_heights:
    total += h
    count += 1

print(round(total / count, 2))