#!/usr/bin/env python


def main():

    answer = input("Greeting: ").lstrip()
    print(f"${value(answer)}")


def value(greeting):

    if greeting.lower().startswith("hello"):
        return 0
    elif greeting[0].lower() == "h":
        return 20
    else:
        return 100


if __name__ == "__main__":
    main()
