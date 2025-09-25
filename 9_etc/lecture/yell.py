#!/usr/bin/env python


def main():
    yell("This", "is", "CS50")


def yell(*words):
    uppercased = map(str.upper, words)
    # upper is a method of the str class. I don't use parenthesis
    # at the end of upper because map will do it for every word
    print(*uppercased)


if __name__ == "__main__":
    main()
