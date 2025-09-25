#!/usr/bin/env python


import argparse

parser = argparse.ArgumentParser(description="Meow like a cat")
parser.add_argument("-n", default=1, help="number of times to meow", type=int)
args = parser.parse_args()
# I now have the object called args inside of which are all of the values
# of those command-line arguments, no matter what order they appear in.

for _ in range(args.n):
    # As I specified that n must be an int, I don't need to convert the arg to an int
    print("meow")
