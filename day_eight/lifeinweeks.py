#!/usr/bin/env python3

def life_in_weeks(age):
    weeks = age * 52
    how_long_left = 4680 - weeks
    print(f"You have {how_long_left} weeks left.")
life_in_weeks(56)