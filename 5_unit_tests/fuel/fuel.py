#!/usr/bin/env python


def main():

    fraction = input("Fraction: ").split("/")
    print(fraction)
    converted = convert(fraction)
    if type(converted) == int:
        print(gauge(converted))
    else:
        main()


def convert(fraction):
    try:
        expression = int(fraction[0]) / int(fraction[1])
    except ValueError:
        print("Must be integers")
    except TypeError:
        print("Must be integers TYPE")
    except ZeroDivisionError:
        print("Can't divide by zero")
    else:
        if int(fraction[0]) < 0 or int(fraction[1]) < 0:
            raise ValueError("Values must be positive")
        elif int(fraction[1]) < int(fraction[0]):
            raise ValueError("Divided can't be superior to divider")
        else:
            return round(expression * 100)


def gauge(percentage):
    if percentage <= 1:
        return "E"
    elif percentage >= 99:
        return "F"
    else:
        return f"{percentage}%"


if __name__ == "__main__":
    main()
