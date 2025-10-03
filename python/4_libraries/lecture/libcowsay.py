#!/usr/bin/env python

import cowsay
import sys


def main():
    if len(sys.argv) == 2:
        cowsay.cow("Hello, " + sys.argv[1])

    # if len(sys.argv) < 2:
    #     sys.exit("Too few arguments")

    # for argument in sys.argv[1:]:
    #     print("Hello, my name is", argument)


# if __name__ == "__main__":
main()
