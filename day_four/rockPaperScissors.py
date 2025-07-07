#!/usr/bin/env python3
import random

scissors = r"""
   _       ,/'
  (_).  ,/'
   _  ::
  (_)'  `\.
           `\.
"""
paper = r"""
 _ __   __ _ _ __   ___ _ __ 
| '_ \ / _` | '_ \ / _ \ '__|
| |_) | (_| | |_) |  __/ |   
| .__/ \__,_| .__/ \___|_|   
| |         | |              
|_|         |_|              
"""

rock = r"""
                _    
               | |   
 _ __ ___   ___| | __
| '__/ _ \ / __| |/ /
| | | (_) | (__|   < 
|_|  \___/ \___|_|\_\           
"""
game_images = [rock, paper, scissors]
player = int(input("Which do you choose? 0 = Rock, 1 = Paper, 2 = Scissors: \n"))
computer = random.randint(0, 2)

if player >= 0 and player <= 3:
    print(game_images[player])
print(f"Computer chose {computer}")
print(game_images[computer])

if player >= 3 or player < 0:
    print("Invalid Number. You Lose!")
elif computer > player:
    print("Computer wins!")
elif player == 2 and computer == 0:
    print("Computer win!")
elif player > computer:
    print("You win!")
elif computer == player:
    print("It's a draw!")
else:
    print("You lose!")