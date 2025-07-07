#!/usr/bin/env python3

import random
random_number = random.randint(0, 1)
print(random_number)

if random_number == 1:
    print("heads")
else:
    print("tails")