#!/usr/bin/env python3
import random

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
players_final_hand = []
computers_hand = []
play = True

def random_card(num_of_cards):
    return random.sample(cards, num_of_cards)

choice = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ").lower()

if choice == 'y':
    players_final_hand = random_card(2)
    player_total = sum(players_final_hand)
    print(f"players cards: {players_final_hand}, current score: {player_total}")
    computers_hand = random_card(2)
    computer_total = sum(computers_hand)
    print(f"computer card: {computers_hand[0]}")
    while play == True:
        another_card = input("Type 'y' to get another card, type 'n' to pass: ")
        if another_card == "y":
            players_final_hand.extend(random_card(1))
            player_total = sum(players_final_hand)
            computers_hand.extend(random_card(1))
            computer_total = sum(computers_hand)
            if player_total == computer_total:
                print(f"\nIt's a draw! Computer's cards: {computers_hand},Computer score: {computer_total}\nYour cards: {players_final_hand} total score: {player_total}")
            elif player_total > 21:
                print(f"\nYou LOSE!\nComputer's cards: {computers_hand},Computer score: {computer_total}\nYour cards: {players_final_hand}, total score: {player_total}")
            elif computer_total > 21 and player_total <= 21:
                print(f"\nYou WIN!\nComputer's cards: {computers_hand},Computer score: {computer_total}, which is over 21! \nYour cards: {players_final_hand}, total score: {player_total}")
            else:
                print(f"players cards: {players_final_hand}, current score: {player_total}\nComputer card: {computers_hand[0]}")       
        else:
            computer_turns = random.choice(True, False)
            while computer_turns == True or computer_total > 21:   
                computers_hand.extend(random_card(1))
                computer_total = sum(computers_hand)
        
            
    


