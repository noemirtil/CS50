#!/usr/bin/env python

import sys


def main():

    if len(sys.argv) < 3:
        try:
            file = sys.argv[1]
        except IndexError:
            print("Too few command-line arguments")
            sys.exit(1)
        else:
            if file.endswith(".py"):
                try:
                    print(count_lines(file))
                except FileNotFoundError:
                    print("File does not exist")
                    sys.exit(1)
            else:
                print("Not a python file")
                sys.exit(1)
    else:
        print("Too many command-line arguments")
        sys.exit(1)


def count_lines(file):
    total = 0
    with open(file) as read:
        for line in read.readlines():
            if (
                line.startswith("#")
                or (line[0] == " " and len(set(line.split("#")[0])) == 1)
                or line == ("\n")
                or (line[0] == " " and len(set(line.split("\n")[0])) == 1)
            ):
                pass
            else:
                total += 1
                # print(f"{total} - {line}", end="")
    return total


if __name__ == "__main__":
    main()
