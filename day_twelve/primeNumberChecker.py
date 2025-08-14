#!/usr/bin/env python3
def is_prime(num):
    if num <= 1:
        return False
    if num <= 3:
        return True    
    if num == 5:
        return True
    if num % 2 == 0 or num % 3 == 0:
        return False
    else:
        return True  
            
if is_prime(5) == True:
    print("It's a prime number.")
else:
    print("It's not a prime number.")   
