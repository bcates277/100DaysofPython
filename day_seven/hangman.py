#!/usr/bin/env python3
import random
from word_list import hangman_words

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

chosen_word = random.choice(hangman_words)
dashes = (len(chosen_word) * "_")

life = 6
game_over = False
correct_letters = []
print(f"Welcome to Hangman!\n{stages[life]}\n{dashes}\nThe word has {len(chosen_word)} letters.")
while game_over == False:
    guessed_letter = input("Guess a letter: ")
    if not guessed_letter.isalpha():
        print("Please enter a letter")
    elif len(guessed_letter) != 1:
        print("Please pick only one letter")
    elif guessed_letter in correct_letters:
        print(f"You already guessed {guessed_letter}. Try Again.")
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
    
    if guessed_letter in correct_letters:
        print(f"Correct! {guessed_letter} is in the word!")

    if guessed_letter not in correct_letters:
        life -= 1
        if life > 1:
            print(f"{stages[life]}\n****Wrong guess! {guessed_letter} is not in the word. Only {life} life left!****\n{display}")
        elif life == 1:
            print(f"{stages[life]}\n****Wrong guess! {guessed_letter} is not in the word. Only {life} life left!****\n{display}")
        else:
            game_over = True
            print(f"{stages[life]}\n****Game Over! {guessed_letter} is not in the word. You have {life} lives left!****\nThe word was {chosen_word}.")
    if display == chosen_word:
            game_over = True
            print(f"You win! The word was {chosen_word}!")
