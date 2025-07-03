#!/usr/bin/env python3

print("Welcome to the tip calculator")

# get total bill 
bill = round(float(input("What was your total bill? ex 212.23: ")), 2)

# get tip percentage
tip = int(input("What percentage would you like to tip? 10, 12, 15, 20? "))

# get number of people
people = int(input("How many people will split the bill? "))

#convert tip percentage to decimal
tip_decimal = tip / 100

# multiple bill by tip percentage to get the tip amount
tip_amount = round((bill) * (tip_decimal), 2)

# bill + tip amount to get the new total
new_total = round((bill) + (tip_amount), 2)


print(f"Bill: ${bill}\n Tip: {tip}%\n Tip as a decimal: {tip_decimal}\n {bill} x {tip_decimal} = {tip_amount}\n ${bill} + ${tip_amount} = ${new_total}")

tip_cal = round(float(new_total) / int(people), 2)

print(f"There are {people} people splitting the bill, so ${new_total} / {people} = ${tip_cal}. Each person should pay: ${round(tip_cal, 2)}")

