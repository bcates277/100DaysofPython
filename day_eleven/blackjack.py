#!/usr/bin/env python3
import random
from logo import blackjack_art

def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    return random.choice(cards)

def compare(user_score, computer_score):
    if user_score == computer_score:
        return ">> Draw!"
    elif computer_score == 0:
        return ">> Lose, opponent has a Blackjack"
    elif user_score == 0:
        return ">> Win, you have a Blackjack"
    elif user_score > 21:
        return ">> You went over 21, you lose"
    elif computer_score > 21:
        return ">> Opponent went over. You win!"
    elif user_score > computer_score:
        return ">> You Win!"
    else:
        return ">> You lose"
    
def calculate_score(cards):
    """calculates the sum of the cards"""
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    if sum(cards) > 21 and 11 in cards:
        cards.remove(11)
        cards.append(1)
    return sum(cards)

    
def play_game():
    print(blackjack_art)
    players_hand = []
    computers_hand = []
    is_game_over = False

    for i in range(2):
        players_hand.append(deal_card())
        computers_hand.append(deal_card())      

    while not is_game_over:   
        user_score = calculate_score(players_hand)
        computer_score = calculate_score(computers_hand) 
        print(f"Your cards: {players_hand}, score: {user_score}\nComputer's card: {computers_hand[0]}")

        if user_score == 0 or computer_score == 0 or user_score >= 21:
            is_game_over = True
        else:
            user_should_deal = input("Type 'y' to get another card, or 'n' to pass: ")
            if user_should_deal == "y":
                players_hand.append(deal_card())
            else:
                is_game_over = True
                
    while computer_score != 0 and computer_score < 17:
        computers_hand.append(deal_card())
        computer_score = calculate_score(computers_hand)

    print(f"-------------\nYour final hand: {players_hand}, score {user_score}\nComputer final hand: {computers_hand}, score: {computer_score}\n--------------")
    print(compare(user_score, computer_score))

while input("Do you want to play a game of BlackJack? Type 'y' or 'n': ") == "y":
    print("\n" * 10)
    play_game()