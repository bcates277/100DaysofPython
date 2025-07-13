#!/usr/bin/env python3

def greeting():
    print("Hello")
    print("How are you?")
    print("bye!")
greeting()

def greet_with_name(name, location):
    print(f"Hello {name} in {location}")
    print(f"How are you? {name}")
    print(f"Bye, {name}!")
greet_with_name("Betsy", "Atlanta")

def greet_with_name(name, location):
    print(f"Hello {name} in {location}")
    print(f"How are you? {name}")
    print(f"Bye, {name}!")
greet_with_name(location="Raleigh", name="Katie")