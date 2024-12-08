# Starter Code

student_scores = {
    "Harry": 81,
    "Ron": 78,
    "Hermione": 99,
    "Draco": 74,
    "Neville": 62
}


# Write your code below!

student_grades = {}

for student in student_scores:
    score  = student_scores[student]
    match score:
        case _ if score > 90:
            student_grades[student] = "A - Outstanding"
        case _ if score > 80:
            student_grades[student] = "B - Exceeds expectations"
        case _ if score > 70:
            student_grades[student] = "C - Acceptable"
        case _ if score < 70:
            student_grades[student] = "F - Failure"

for key in student_grades:
    print(f"{key} has a grade of '{student_grades[key]}'")