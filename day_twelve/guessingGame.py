#!/usr/bin/env python3
import random
print("Welcome to the number guessing game! Chose")
level = input("Choose a difficulty. Type 'easy' or 'hard': ")

random_number = random.randint(1, 100)

if level == "easy":
    attempts = 10
else:
    attempts = 5
    
while attempts > 0:
    print(f"You have {attempts} attempts remaining to guess the number.")
    guess = int(input("Make a guess: "))
    
    if guess < random_number:
        print("Too low.")
        attempts -= 1
    elif guess > random_number:
        print("Too high.")
        attempts -= 1
    else:
        print(f"You got it! The answer was {random_number}.")
        break
if attempts == 0:
    print("You've run out of guesses, you lose.")
    print(f"The correct number was {random_number}.")