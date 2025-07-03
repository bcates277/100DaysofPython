#!/Users/betsycates/Documents/Python/.venv/bin/python

print("hello"[-2])

#string
print("123" + "456")

# Integer = whole number
print(123 + 456)

# Float = decimal number
print(123.456 + 456.789)

# boolean
print(True)
print(False)

print(type(False))
print(type(123))
print(type(123.456))
print(type("hello"))

print("Number of letters in your name: " + str(len(input("What is your name? "))))

print(123 + 456)
print(3-2)
print(3*2)
print(6/3)
print(6//3)  # Integer division
print(7//3)  # Integer division
print(7/3)   # Float division
print(6%3)   # Modulus (remainder of division)
print(13%3)   # Modulus (remainder of division)
print(2**3)  # 2 to the power of 3

# PEMDASLR 
# ()
# **
# *
# /
# +
# -

print(3 * 3 + 3 / 3 - 3)
print((3 * 3 / 3) - 3 + 3)

height = 1.65 
weight = 84

# Write your code here.
# Calculate the bmi using weight and height.
bmi = weight / (height ** 2)

print("BMI is: " + str(bmi))
print("BMI rounded up or down: " + str(round(bmi)))
print("BMI rounded down: " + str(int(bmi)))
print("BMI rounded to 2 decimal places: " + str(round(bmi, 2)))  # Round to 2 decimal places
