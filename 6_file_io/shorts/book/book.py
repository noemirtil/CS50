#!/usr/bin/env python


def main():
    with open("alice.txt") as r, open("chapter1.txt", "w") as w:
        w.writelines(r.readlines()[52:286])


if __name__ == "__main__":
    main()
