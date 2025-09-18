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
        elif matches.group("am_h") in ("10", "11"):
            am_h = matches.group("am_h")
        else:
            am_h = f"0{matches.group("am_h")}"
        if matches.group("pm_h") == "12":
            pm_h = "12"
        else:
            pm_h = int(matches.group("pm_h")) + 12
        if matches.group("am_m"):
            am_m = matches.group("am_m")
        else:
            am_m = ":00"
        if matches.group("pm_m"):
            pm_m = matches.group("pm_m")
        else:
            pm_m = ":00"
        return f"{am_h}{am_m} to {pm_h}{pm_m}"
    elif matches := re.fullmatch(
        r"^(?P<pm_h>[1-9]|(1[012]))(?P<pm_m>:[0-5]\d)? PM to (?P<am_h>[1-9]|(1[012]))(?P<am_m>:[0-5]\d)? AM$",
        s,
    ):
        if matches.group("am_h") == "12":
            am_h = "00"
        elif matches.group("am_h") in ("10", "11"):
            am_h = matches.group("am_h")
        else:
            am_h = f"0{matches.group("am_h")}"
        if matches.group("pm_h") == "12":
            pm_h = "12"
        else:
            pm_h = int(matches.group("pm_h")) + 12
        if matches.group("am_m"):
            am_m = matches.group("am_m")
        else:
            am_m = ":00"
        if matches.group("pm_m"):
            pm_m = matches.group("pm_m")
        else:
            pm_m = ":00"
        return f"{pm_h}{pm_m} to {am_h}{am_m}"
    else:
        raise ValueError("Wrong format")


if __name__ == "__main__":
    main()
