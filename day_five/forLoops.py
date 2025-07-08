#!/usr/bin/env python3

fruits = ["Strawberries", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears"]
for fruit in fruits:
    print(fruit)
    print(fruit + " Pie")
    
student_scores = [78, 65, 89, 90, 98, 100]
max_score = 0
print(max(student_scores))
for score in student_scores:
    if score > max_score:
        max_score = score
print(max_score)