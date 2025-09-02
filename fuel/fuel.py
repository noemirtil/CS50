#!/usr/bin/env python


def main():

    nums = input("Fraction: ").split("/")
    try:
        fraction = int(nums[0]) / int(nums[1])
    except ValueError:
        print("Not int / int")
    except ZeroDivisionError:
        print("Can't divide by 0")
    else:

        percent = round(fraction * 100, 2)
        if percent <= 1:
            print("E")
        elif percent >= 99:
            print("F")
        else:
            print(f"{percent}%")


main()
