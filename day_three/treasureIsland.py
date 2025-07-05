#!/usr/bin/env python3

#!/usr/bin/env python3

print(r"""
                            _.--.
                        _.-'_:-'||
                    _.-'_.-::::'||
               _.-:'_.-::::::'  ||
             .'`-.-:::::::'     ||
            /.'`;|:::::::'      ||_
           ||   ||::::::'     _.;._'-._
           ||   ||:::::'  _.-!oo @.!-._'-.
           \'.  ||:::::.-!()oo @!()@.-'_.|
            '.'-;|:.-'.&$@.& ()$%-'o.'\U||
              `>'-.!@%()@'@_%-'_.-o _.|'||
               ||-._'-.@.-'_.-' _.-o  |'||
               ||=[ '-._.-\U/.-'    o |'||
               || '-.]=|| |'|      o  |'||
               ||      || |'|        _| ';
               ||      || |'|    _.-'_.-'
               |'-._   || |'|_.-'_.-'
                 '-._'-.|| |' `_.-'
                    '-.||_/.-'
""")


print("Welcome to treasure island!\nYour mission is to find the treasure.")
direction = input('Which direction do you want to go? Type "left" or "right": ').lower()
if direction == "left":
    action = input('Do you want to swim or wait? Type "swim" or "wait": ').lower()
    if action == "wait":
        door = input('You arrive at a lake with three doors. Which door do you want to open? Type "red", "blue", or "yellow": ').lower()
        if door == "red":
            print("You found a room full of fire. Game over.")
            exit()
        elif door == "blue":
            print("You found a room full of beasts. Game over.")
            exit()
        elif door == "yellow":
            print("You found the treasure! You win!")
            exit()
        else:
            print("You chose a door that doesn't exist. Game over.")
            exit()
    else:
        print("You got attacked by a trout. Game over.")
        exit()
else:
    print("You fell into a hole. Game over.")
    exit()
