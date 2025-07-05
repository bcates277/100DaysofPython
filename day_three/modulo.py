#!/usr/bin/env python3

# This script checks if a number is even or odd using the modulo operator.
number_to_test = int(input("Enter a number to test if it is even or odd: "))

# Calculate the remainder when dividing by 2
remainder = number_to_test % 2 

# Check if the number is even or odd
# If the remainder is 0, it is even; otherwise, it is odd
# Using an if statement to determine even or odd
if number_to_test % 2  == 0:
    print(f"You number, {number_to_test} is an even number")
else:
    print(f"You number, {number_to_test} is an odd number, the remainder is {remainder}")
    