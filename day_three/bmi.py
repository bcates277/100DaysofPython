#!/usr/bin/env python3

weight = 65
height = 1.85

bmi = weight / (height ** 2)

print(f"BMI is: {bmi}")

if bmi < 18.5:
    print("underweight")
elif bmi >= 18.5 and bmi < 25:
    print("normal weight")
else:
    print("overweight")