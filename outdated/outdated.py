#!/usr/bin/env python

months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December",
]


def main():

    while True:
        entry = input("Date: ")

        if (entry[0]).isdecimal():
            try:
                entries = entry.split("/")
                print(f"{int(entries[2])}-{int(entries[0]):02}-{int(entries[1]):02}")
                break
            except (IndexError, ValueError):
                continue
        elif (entry[0]).isalpha():
            try:
                entries = entry.split(" ")
                if (entries[0]) in months:
                    print(
                        f"{entries[2]}-{(months.index(entries[0]) + 1):02}-{int(entries[1]):02}"
                    )
                    break
            except (IndexError, ValueError):
                continue
        else:
            continue


main()
