#!/usr/bin/env python


def main():
    vowels = ["a", "e", "i", "o", "u", "A", "E", "I", "O"]
    text = input("Input: ")

    i = 0
    while i < (len(text) - 1):
        if text[i] in vowels:
            pass
        else:
            print(text[i], end="")
        i += 1
    if text[len(text) - 1] in vowels:
        print("")
    else:
        print(text[i])


main()
