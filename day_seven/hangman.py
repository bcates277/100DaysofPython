#!/usr/bin/env python3
import random

stages = [r"""
      _______
     |/      |
     |      
     |      
     |      
     |      
     |
    _|___
 """,
 r"""
      _______
     |/      |
     |      ( )
     |      
     |       
     |     
     |
    _|___
 """,
r"""
      _______
     |/      |
     |      (_)
     |      
     |       
     |      
     |
    _|___
 """,
r"""
      _______
     |/      |
     |      (_)
     |      \|/
     |       
     |      
     |
    _|___
 """,
r"""
      _______
     |/      |
     |      (_)
     |      \|/
     |       |
     |      
     |
    _|___
 """,
r"""
      _______
     |/      |
     |      (_)
     |      \|/
     |       |
     |      / 
     |
    _|___
 """,
r"""
      _______
     |/      |
     |      (_)
     |      \|/
     |       |
     |      / \
     |
    _|___
 """
 ]

random_word_list = ['giraffe']

chosen_word = random.choice(random_word_list)
print(chosen_word)
placeholder = (len(chosen_word) * "_")
print(placeholder)

life = 6
game_over = False
correct_letters = []
print(f"Welcome to Hangman!\n{stages[life]}")
while game_over == False:
    guessed_letter = input("Guess a letter: ")
    if not guessed_letter.isalpha():
        print("Please enter a letter")
    elif len(guessed_letter) != 1:
        print("Please pick only one letter")
    else:
        display = ""
        for letter in chosen_word:
            if letter == guessed_letter:
                display += letter
                correct_letters.append(letter)
            elif letter in correct_letters:
                display += letter
            else:
                display += "_"
    print(display)

    if guessed_letter not in correct_letters:
        life -= 1
        if life > 1:
            print(f"Wrong guess! Only {life} lives left\n{stages[life]}\n{display}")
        elif life == 1:
            print(f"Wrong guess! Only {life} life left\n{stages[life]}\n{display}")
        else:
            game_over = True
            print(f"Game Over! You have {life} lives left\n{stages[life]}\nThe word was {chosen_word}.")
    if display == chosen_word:
            game_over = True
            print(f"You win! The word was {chosen_word}")
