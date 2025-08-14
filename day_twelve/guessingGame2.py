#!/usr/bin/env python3
import random

EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5

def check_guess(guess, answer, turns):
    if guess < answer:
        print("Too low.")
        return turns - 1
    elif guess > answer:
        print("Too high.")
        return turns - 1
    else:
        print(f"You got it! The answer was {answer}.")
        
def set_difficulty():
    level = input("Choose a difficulty. Type 'easy' or 'hard': ")
    if level == "easy":
        return EASY_LEVEL_TURNS
    else:
        return HARD_LEVEL_TURNS
    


def game():
    print("Welcome to the number guessing game!")
    print("I'm thinking of a number between 1 and 100.")
    answer = random.randint(1, 100)
    turns = set_difficulty()
    guess = 0
    
    while guess != answer:
        if turns > 0:
            guess = int(input(f"You have {turns} attempts remaining. Make a guess: "))
            turns = check_guess(guess, answer, turns)
        else:
            print("You've run out of guesses, you lose.")
            print(f"The correct number was {answer}.")
            break
    else:
        print(f"You got it! The answer was {answer}.")  
game()