#!/usr/bin/env python3

for number in range(1, 101):
    if number % 3 == 0 and number % 5 == 0:
        print("FizzBuzz")
    elif number % 3 == 0:
        print("fizz")
    elif number % 5 == 0:
        print("Buzz!")
    else:
        print(number)