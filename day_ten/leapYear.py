#!/usr/bin/env python3


def is_leap_year(year):
    if year % 4 == 0:
        return is_leap_year_1(year)
    else:
        return False
def is_leap_year_1(year):
    """check year and see if 
    it is divisible by 100"""
    if year % 100 != 0:
        return True
    else:
        return is_leap_year_2(year)
def is_leap_year_2(year):
    if year % 400 == 0:
        return True
    else:
        return False

ok = is_leap_year(1700)
print(ok)
    




# - on every year that is divisible by 4 with no remainder

# - except every year that is evenly divisible by 100 with no remainder 

# - unless the year is also divisible by 400 with no remainder  