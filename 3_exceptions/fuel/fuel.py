#!/usr/bin/env python


def main():

    while True:
        nums = input("Fraction: ").split("/")

        try:
            fraction = int(nums[0]) / int(nums[1])
        except (ZeroDivisionError, ValueError):
            continue
        if int(nums[0]) < 0 or int(nums[1]) < 0 or int(nums[1]) < int(nums[0]):
            continue
        else:
            percent = round(fraction * 100)
            if percent <= 1:
                print("E")
            elif percent >= 99:
                print("F")
            else:
                print(f"{percent}%")
        break


main()
