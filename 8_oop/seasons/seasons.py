#!/usr/bin/env python

from datetime import date
import inflect
import re
import sys


def main():
    birthdate = input("Date of Birth: ").strip()
    number_minutes = count_minutes(check_birthdate(birthdate))
    p = inflect.engine()
    words_minutes = p.number_to_words(number_minutes)
    print(f"{words_minutes.capitalize()} minutes")


def check_birthdate(birthdate):
    if re.fullmatch(r"\d{4}-[01]?\d-\d{2}", birthdate):
        year, month, day = birthdate.split("-")
        return date(int(year), int(month), int(day))
    else:
        print("Invalid date")
        sys.exit(0)


def count_minutes(birthdate):
    number_of_days = date.today() - birthdate
    return number_of_days.days * 24 * 60


if __name__ == "__main__":
    main()
