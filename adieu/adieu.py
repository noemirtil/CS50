#!/usr/bin/env python

import inflect


def main():

    names = []

    while True:
        try:
            text = input("Name: ")
            names.append(text)

        except EOFError:
            print(f"\nAdieu, adieu, to {inflect.engine().join(names)}")
            break


if __name__ == "__main__":
    main()
