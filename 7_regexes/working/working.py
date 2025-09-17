#!/usr/bin/env python

import re
import sys


def main():
    print(convert(input("Hours: ").strip()))


def convert(s):
    if matches := re.fullmatch(
        r"^(?P<am_h>[1-9]|(1[012]))(?P<am_m>:[0-5]\d)? AM to (?P<pm_h>[1-9]|(1[012]))(?P<pm_m>:[0-5]\d)? PM$",
        s,
    ):
        if matches.group("am_h") == "12":
            am_h = "00"
        else:
            am_h = matches.group("am_h")
        if matches.group("pm_h") == "12":
            pm_h = "12"
        else:
            pm_h = int(matches.group("pm_h")) + 12
        return f"{am_h}{matches.group("am_m")} to {pm_h}{matches.group("pm_m")}"


if __name__ == "__main__":
    main()
