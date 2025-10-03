#!/usr/bin/env python

import sys
import csv
import os.path
from tabulate import tabulate


def main():
    check_arguments()
    with open(sys.argv[1]) as file:
        # Create list "header" with first line of CSV file:
        header = ((file.readlines()[0])).replace("\n", "").split(",")
        # Check if header corresponds to Pinocchio's format:
        if not len(header) == 3 and header[1] == "Small" and header[2] == "Large":
            print("CSV is not in Pinocchio's format")
        else:
            # Create a dictionary of lists as values with header items (columns) as keys:
            dict = {}
            for column in header:
                dict[column] = []
                with open(sys.argv[1]) as file:
                    # Necessary to open it every time unless result stored in a variable
                    reader = csv.DictReader(file)
                    for row in reader:
                        # Append each read row to each list (value) according to its column (key) name:
                        dict[column].append(row[column])
            print(tabulate(dict, headers="keys", tablefmt="grid"))


def check_arguments():
    if len(sys.argv) == 1:
        print("Too few command-line arguments")
    elif len(sys.argv) > 2:
        print("Too many command-line arguments")
    elif not sys.argv[1].endswith(".csv"):
        print("Not a CSV file")
    elif not os.path.isfile(sys.argv[1]):
        print("File doesn't exist")
    else:
        return
    sys.exit(1)


if __name__ == "__main__":
    main()
