#!/usr/bin/env python


def main():
    answer = input("Greeting: ").lstrip().lower()

    if answer.startswith("hello"):
        print("$0")
    elif answer[0] == "h":
        print("$20")
    else:
        print("$100")


main()
