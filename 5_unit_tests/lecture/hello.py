#!/usr/bin/env python


def main():
    name = input("What's your name? ")
    print(say_hello(name))


def say_hello(to="world"):
    return f"Hello, {to}"


if __name__ == "__main__":
    main()
