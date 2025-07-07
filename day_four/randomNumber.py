#!/usr/bin/env python3

import random
import myModule

random_int = random.randint(1, 10)  # Generates a random integer between 1 and 10
print(random_int)
print(myModule.my_fav_num)  # Accessing the variable from myModule

random_number_0_to_1 = random.random() * 10  # Generates a random float between 0.0 and 1.0
print(random_number_0_to_1)

random_float = random.uniform(1, 10)  # Generates a random float between 1.0 and 10.0
print(random_float)