#!/usr/bin/env python3

def calculate_love_score(name1, name2):
    true = "true"
    love = "love"
    total_true = 0
    total_love = 0
    for letter in true:
        total_true += name1.lower().count(letter.lower())
        total_true += name2.lower().count(letter.lower())
    for letter in love:
        total_love += name1.lower().count(letter.lower())
        total_love += name2.lower().count(letter.lower())
    total = str(total_true) + str(total_love)
    print(total)
calculate_love_score("Kanye West", "Kim Kardashian")