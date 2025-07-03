#!/usr/bin/env python3

line = "------------------"

# Print seperate lines with """
print("""1. Mix 500g of Flour, 10g Yeast and 300ml Water in a bowl.
2. Knead the dough for 10 minutes.
3. Add 3g of Salt.
4. Leave to rise for 2 hours.
5. Bake at 200 degrees C for 30 minutes.""")

print(line)

# Print a single line with \n
print("1. Mix 500g of Flour, 10g Yeast and 300ml Water in a bowl.\n2. Knead the dough for 10 minutes.\n3. Add 3g of Salt.\n4. Leave to rise for 2 hours.\n5. Bake at 200 degrees C for 30 minutes.")

print(line)

# Concatenation of strings
print("hello" + " " + "Karen")

print(line)

# input() function
print("Hello " + input("what is your name? ") + "!")

print(line)

#variable assignment
animal = input("What is your favorite animal? ")
print(animal)

print(line)

# length
print(len(input("What is your favorite food? ")))

print(line)

# variable assignment and length
food = input("What is your favorite color? ")
length = len(food)
print(length)

print(line)

#switching variables
glass1 = "milk"
glass2 = "juice"
temp = glass1
glass1 = glass2
glass2 = temp
print(glass1, glass2)

