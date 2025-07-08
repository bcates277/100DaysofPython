#!/usr/bin/env python3

import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm','n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input("How many symbols would you like?\n"))
nr_numbers = int(input("How many numbers would you like?\n"))

# Password List
new_password_list = []
for letter in range(0, nr_letters):
    new_password_list.append(random.choice(letters))

for symbol in range(0, nr_symbols):
    new_password_list.append(random.choice(symbols))

for number in range(0, nr_numbers):
    new_password_list.append(random.choice(numbers))

password = ""
for char in new_password_list:
    password += char
print(f"Your password is: {password}")
    

# # Password String
# new_password = ""
# for letter in range(0, nr_letters):
#     new_password += random.choice(letters)
    
# for symbol in range(0, nr_symbols):
#     new_password += random.choice(symbols)

# for number in range(0, nr_numbers):
#     new_password += random.choice(numbers)

# print(new_password)
    