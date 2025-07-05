#!/usr/bin/env python3

print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
bill = 0

if height >= 120:
    print("You can ride the rollercoaster")
    age = int(input("what is your age? "))
    if age <= 12:
        bill = 5
        print("Please pay $5 for a child's ticket.")
    elif age <= 18:
        bill = 7
        print("Please pay $7 for a youth ticket. ")
    elif 45<= age <=55:
        print("Your ticket is free, enjoy the ride!")
    else:
        bill = 12
        print("Please pay $12 for an adult ticket. ")
    wants_photo = str(input("Do you want a photo taken? Y or N: ")).upper()
    if wants_photo == "Y":
        bill += 3
    print(f"Your total bill is ${bill}.")
    
else:
    print("Sorry, you have to be 120 cm or taller to ride the roller coaster.") 
    