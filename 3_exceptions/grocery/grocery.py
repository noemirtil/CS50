#!/usr/bin/env python


def main():
    to_buy = {}

    while True:
        try:
            item = input("").upper()
        except EOFError:
            for _ in sorted(to_buy):
                print(f"{to_buy[_]} {_}")
            break
        else:
            if item not in to_buy:
                to_buy[item] = 1
            else:
                to_buy[item] += 1
            # print(to_buy)


main()
