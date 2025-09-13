#!/usr/bin/env python

import sys


def main():

    try:
        string = input("Fraction: ")
    except EOFError:
        print("See you later!")
        sys.exit(0)
    else:
        converted = convert(string)
        print(gauge(converted))


def convert(string):
    list = string.split("/")
    try:
        fraction = int(list[0]) / int(list[1])
    except ValueError:
        raise ValueError("Must be integers")
        # print("Must be integers")
        # main()
    except ZeroDivisionError:
        raise ZeroDivisionError("Can't divide by zero")
        # print("Can't divide by zero")
        # main()
    else:
        if int(list[0]) < 0 or int(list[1]) < 0:
            raise ValueError("Values must be positive")
        elif int(list[1]) < int(list[0]):
            raise ValueError("Divided can't be superior to divider")
        else:
            return round(fraction * 100)


def gauge(percentage):
    if percentage <= 1:
        return "E"
    elif percentage >= 99:
        return "F"
    else:
        return f"{percentage}%"


if __name__ == "__main__":
    main()
