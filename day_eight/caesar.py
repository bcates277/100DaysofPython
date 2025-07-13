#!/usr/bin/env python3

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
            'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = str(input("Type 'encode' to encrypt, type 'decode' to decrypt: \n").lower())
if direction == "encode" or direction == "decode":
    text = input("Type your message: \n").lower()
    shift = int(input("Type the shift number: \n"))
else:
    print(f"Please type a correct response {exit()}")
    

list1 = []
list2 = []
def encrypt():
    if direction == "encode":
        for letters in text:
            list1.append(alphabet.index(letters))
        for num in range(len(list1)):
            list1[num] += shift
        for nums in list1:
            list2.append(alphabet[nums])
            
    else:
        print("no")
    print(list1, "".join(list2))

encrypt()
