#!/usr/bin/env python3

print("Welcome to the Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L: ").upper()
if size not in ["S", "M", "L"]:
    print("Please choose a correct size pizza, S, M, or L.")
    exit()
pepperoni = input("Do you want pepperoni on your pizza? Y or N: ").upper()
if pepperoni not in ["Y", "N"]:
    print("Please choose a correct option for pepperoni, Y or N.")
    exit()
extra_cheese = input("Do you want extra cheese? Y or N: ").upper()
if extra_cheese not in ["Y", "N"]:
    print("Please choose a correct option for extra cheese, Y or N.")
    exit()
bill = 0

if size == "S":
    bill += 15
elif size == "M":
    bill += 20
else:
    bill += 25
    
if pepperoni == "Y":
    if size == "S":
        bill += 2
    else:
        bill += 3
if extra_cheese == "Y":
    bill += 1
    
print(f"Your final bill is: ${bill}.")

