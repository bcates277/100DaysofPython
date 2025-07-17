#!/usr/bin/env python3

def add(n1, n2):
    return n1 + n2

def sub(n1, n2):
    return n1 - n2

def multi(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

operations = {
    "+": add,
    "-": sub,
    "*": multi,
    "/": divide 
}

# print(operations["*"](4, 8))

def calculator ():
    calculations = True
    num1 = float(input("What's the first number? "))

    while calculations:
        num2 = float(input("What's the next number? "))
        for key in operations:
            print(key)

        chosen_operation = input("Pick an operation: ")

        answer = (operations[chosen_operation](num1, num2))
        print(f"{num1} {chosen_operation} {num2} = {answer}")
        _next = input(f"Type 'y' to continue calculating with {answer}, type 'n' to start a new calculation, or 'e' to exit: ").lower()
        if _next == "y":
            num1 = answer
        elif _next == "n":
            calculations = False
            print("\n" * 20)
            calculator()
        else:
            exit()

calculator()
        


        