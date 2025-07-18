#!/usr/bin/env python3
import random

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
players_final_hand = []
computers_hand = []

def random_card(num_of_cards):
    return random.sample(cards, num_of_cards)

computer_turns = random.choice([True, False])
print(computer_turns)
while random.choice([True, False]) or sum(computers_hand) >= 21:
    computers_hand.extend(random_card())
    
print(f"Computers card: {computers_hand}, computer total: {computer_total}")