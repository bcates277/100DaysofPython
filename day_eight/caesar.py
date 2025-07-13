#!/usr/bin/env python3

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
            'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    
def caesar(original_text, shift_amount, encode_or_decode):
    output = ""
    if encode_or_decode == 'decode':
        shift_amount *= -1
    for letters in original_text:
        if letters not in alphabet:
            output += letters
        else:
            shifted = (alphabet.index(letters) + shift_amount)
            shifted %= len(alphabet)
            output += alphabet[shifted]
    print(f"Here is the {encode_or_decode}d result: {output}")
should_continue = True
while should_continue: 
    direction = str(input("Type 'encode' to encrypt, type 'decode' to decrypt: \n").lower())
    if direction == "encode" or direction == "decode":
        text = input("Type your message: \n").lower()
        shift = int(input("Type the shift number: \n"))
    else:
        print(f"Please type a correct response {exit()}") 
        
    caesar(text, shift, direction)
    print("____________________________________________\n")
    restart = input("Type 'yes' to continue, 'no' to end\n").lower()
    if restart == "no":
        should_continue = False
        print("goodbye")
    elif restart == "yes":
        should_continue = True
    else:
        exit()