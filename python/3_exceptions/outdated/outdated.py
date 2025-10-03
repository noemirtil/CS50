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
        try:
            entry = input("Date: ")
        except EOFError:
            break
        else:
            if all(_.isdecimal() or _ == "/" or _ == " " for _ in entry):
                entries = entry.split("/")
                entries = [int(_) for _ in entries]
                if (
                    len(entries) != 3
                    or not 0 < entries[0] <= 12
                    or not 0 < entries[1] <= 31
                    or not 0 < entries[2] <= 9999
                ):
                    continue
                else:
                    print(
                        f"{int(entries[2]):04}-{int(entries[0]):02}-{int(entries[1]):02}"
                    )
                    break

            elif (entry[0]).isalpha():
                if all(
                    _.isdecimal() or _.isalpha() or _ == " " or _ == "," for _ in entry
                ):
                    entries = entry.split(" ")
                    if entries[1][-1] == ",":
                        entries[1] = entries[1].replace(",", "")
                        if (
                            len(entries) != 3
                            or not entries[0].isalpha()
                            or not entries[1].isdecimal()
                            or not entries[2].isdecimal()
                        ):
                            continue
                        else:
                            entries = [entries[0], int(entries[1]), int(entries[2])]
                            if (
                                not entries[0] in months
                                or not 0 < entries[1] <= 31
                                or not 0 < entries[2] <= 9999
                            ):
                                continue
                            else:
                                print(
                                    f"{entries[2]:04}-{(months.index(entries[0]) + 1):02}-{entries[1]:02}"
                                )
                                break
                    else:
                        continue
            else:
                continue


main()
