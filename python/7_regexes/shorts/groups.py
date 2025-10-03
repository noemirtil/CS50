#!/usr/bin/env python

import re

locations = {"+1": "United States and Canada", "+62": "Indonesia", "+505": "Nicaragua"}


def main():
    pattern = r"(?P<country_code>\+\d{1,3}) \d{3}-\d{3}-\d{4}"
    number = input("Number: ")

    if match := re.search(pattern, number):
        country_code = match.group("country_code")
        print(locations.get(country_code, country_code))
    # .get(key, default value) returns None (by default) or a user-specified default value when the requested key is not found
    else:
        print("Invalid")


if __name__ == "__main__":
    main()
