#!/usr/bin/env python

menu = {
    "Baja Taco": 4.25,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00,
}

import string


def main():
    total = 0
    while True:
        try:
            key = string.capwords(input("Item: \n"))
        except EOFError:
            break
        if not key in menu:
            continue
        else:
            total += menu[key]
            print(f"Total: ${total:.2f}")


main()
