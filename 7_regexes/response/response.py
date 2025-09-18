#!/usr/bin/env python

# import validators
from validator_collection import is_email


def main():
    email = input("What's your email address? ")
    print(validate(email))


def validate(s):
    return "Valid" if is_email(s) else "Invalid"


if __name__ == "__main__":
    main()
