#!/usr/bin/env python

import re


def main():
    code = input("Hexadecimal color code: ")

    pattern = r"^#[a-f0-9]{6}$"
    if match := re.search(pattern, code, re.I):
        print(f"Valid. Matched with {match.group()}")
    else:
        print("Invalid.")


if __name__ == "__main__":
    main()
