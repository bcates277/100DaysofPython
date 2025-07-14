#!/usr/bin/env python3

capitals = {
    "France": "Paris",
    "Germany": "Berlin"
}

travel_log = {
    "France": ["Paris", "Lille", "Dijon"],
    "Germany": ["Stuttgart", "Berlin"]
}
print(travel_log["France"][1])

nested_list = ["A", "B", ["C", "D"]]
print(nested_list[2][0])

travel_log_1 = {
    "France": {
        "num_times_visited": 8,
        "cities_visited": ["Paris", "Lille", "Dijon"],
               },
    "Germany": {
        "num_times_visited": 5,
        "cities_visited": ["Berlin", "Hamburg", "Stuttgart"],
               },
}
print(travel_log_1["Germany"]["cities_visited"][2])

order = {
    "starter": {1: "Salad", 2: "Soup"},
    "main": {1: ["Burger", "Fries"], 2: ["Steak"]},
    "dessert": {1: ["Ice Cream"], 2: []},
}
print(order["main"][2])

starting_dictionary = {
    "a": 9,
    "b": 8,
}


final_dictionary = {
    "a": 9,
    "b": 8,
    "c": 7,
}
starting_dictionary["c"] = 7
final_dictionary = starting_dictionary
print(final_dictionary)

dict = {
    "a": 1,
    "b": 2,
    "c": 3,
}
dict[1] = 4
print(dict)