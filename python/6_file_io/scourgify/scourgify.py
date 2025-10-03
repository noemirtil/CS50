#!/usr/bin/env python

import sys
import csv
import os.path


def main():
    check_arguments()
    with open(sys.argv[1]) as r, open(sys.argv[2], "w") as w:
        writer = csv.DictWriter(w, fieldnames=["first", "last", "house"])
        writer.writeheader()
        reader = csv.DictReader(r)
        for line in reader:
            writer.writerow(
                {
                    "first": line["name"].split(",")[1].strip().replace("\n", ""),
                    "last": line["name"].split(",")[0].strip().replace("\n", ""),
                    "house": line["house"].strip().replace("\n", ""),
                }
            )
    sys.exit(0)
    # with open(sys.argv[2]) as r_a:
    #     print(r_a.readlines())


def check_arguments():
    if len(sys.argv) < 3:
        print("Too few command-line arguments")
    elif len(sys.argv) > 3:
        print("Too many command-line arguments")
    elif not sys.argv[1].endswith(".csv") or not sys.argv[2].endswith(".csv"):
        print("Not a CSV file")
    elif not os.path.exists(sys.argv[1]):
        print(f"Could not read {sys.argv[1]}")
    else:
        if check_format():
            return
    sys.exit(1)


def check_format():
    with open(sys.argv[1]) as r:
        try:
            read = r.readlines()[0].replace("\n", "").split(",")
        except IndexError:
            print("CSV doesn't have a first line")
        else:
            if read == ["name", "house"]:
                return True
            else:
                print("CSV format is not name,house")


if __name__ == "__main__":
    main()
