#!/usr/bin/env python3

import random

# Option 1: Using random.randint to select a random friend
friends = ["Alice", "Bob", "Charlie", "David", "Eve"]
random_number = random.randint(0, 4)
print(friends[random_number])

# Option 2: Using random.choice to select a random friend
print(random.choice(friends))

# print length of the list
print(len(friends))

# Dirty Dozen Example
fruits = ["Strawberries", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears"]
vegetables = ["Spinach", "Kale", "Tomatoes", "Celery", "Potatoes"]
 
dirty_dozen = [fruits, vegetables]
 
print(dirty_dozen[1][1])