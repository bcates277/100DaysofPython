#!/usr/bin/env python3

image = r"""
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\
                         `'-------'`
                       .-------------.
                      /_______________\
                       """
print(f"{image}\nWelcome to the Silent Auction!\n")
bids = True
bidding_dictionary = {}
while bids == True:
    name = str(input("What is your name?\n"))
    bid = int(input("How much money do you want to bid?\n$"))
    bidding_dictionary[name] = bid
    next = input("Does anyone else want to place a bid? 'Y' or 'N'?\n").upper()
    if next == "N":
        bids = False
        winner = max(bidding_dictionary, key=bidding_dictionary.get)
        print(f"The winner is {winner} with a ${bidding_dictionary[winner]} bid!")
    elif next == "Y":
        print("\n" * 100)
        bids = True
        