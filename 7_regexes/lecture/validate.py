#!/usr/bin/env python

import re


def main():

    name = input("What's your name? ").strip()
    if matches := re.search(r"^(.+), *(.+)$", name):
        name = matches.group(2) + " " + matches.group(1)
    print(f"hello, {name}")


if __name__ == "__main__":
    main()
