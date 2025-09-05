#!/usr/bin/env python

import emoji


def main():
    code = input("Input: ")
    print(f"Output: {emoji.emojize(code, language='alias')}")


if __name__ == "__main__":
    main()
