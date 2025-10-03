#!/usr/bin/env python


def main():
    x = int(input("What's x? "))
    print("x squared is", square(x))


def square(n):
    return n * n


def entry():
    return input("What's x? ")


if __name__ == "__main__":
    main()
