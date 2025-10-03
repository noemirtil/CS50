#!/usr/bin/env python


def main():
    text = input("Input: ")
    print(shorten(text))


def shorten(word):
    vowels = ["a", "e", "i", "o", "u", "A", "E", "I", "O"]
    new_text = []
    for char in word:
        if char in vowels or not char.isalpha():
            pass
        else:
            new_text.append(char)
    return "".join(new_text)


if __name__ == "__main__":
    main()
