#!/usr/bin/env python

import sys
import random
from pyfiglet import Figlet

figlet = Figlet()


def to_ascii(t, f):
    figlet.setFont(font=f)
    print(figlet.renderText(t))


def main():
    if len(sys.argv) == 1 or (
        len(sys.argv) == 3
        and sys.argv[1] in ("-f", "--font")
        and sys.argv[2] in figlet.getFonts()
    ):
        try:
            text = input("Input: ")

            if len(sys.argv) == 1:
                to_ascii(text, random.choice(figlet.getFonts()))

            else:
                to_ascii(text, sys.argv[2])

        except EOFError:
            sys.exit("Goodbye!")

    else:
        sys.exit("Invalid usage")


if __name__ == "__main__":
    main()
