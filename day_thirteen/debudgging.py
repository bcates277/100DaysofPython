#!/usr/bin/env python3

try:
    age = int(input("What is your age? "))
except ValueError:
    print("Please enter a valid number.")
    age = int(input("What is your age? "))

if age >= 18:
    print("You can vote!")
else:
    print("You cannot vote yet.")