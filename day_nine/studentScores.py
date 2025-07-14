#!/usr/bin/env python3

student_scores = {
    'Harry': 88,
    'Ron': 78,
    'Hermione': 95,
    'Draco': 75,
    'Neville': 60
}

# Student's name are keys.
# Prints the value of Harry = 88
# print(student_scores['Harry'])

student_grades = {}

for keys in student_scores:
    # Keys are student's names
    grade = student_scores[keys] # Each student's score = the variable grade
    if 91 <= grade <= 100:
        student_grades[keys] = ("Outstanding") # Changes the value
    elif 81 <= grade <= 90:
        student_grades[keys] = ("Exceeds Expectations")
    elif 71 <= grade <= 80:
        student_grades[keys] = ("Acceptable")
    else:
        student_grades[keys] = ("Fail")

print(student_grades)