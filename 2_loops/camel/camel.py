#!/usr/bin/env python


def main():
    snake_case = input("Enter a word in camelCase: ")

    i = 0
    while i < (len(snake_case) - 1):
        if snake_case[i].islower():
            print(snake_case[i], end="")
        elif snake_case[i].isupper():
            print("_" + snake_case[i].lower(), end="")
        i += 1
    if snake_case[len(snake_case) - 1].islower():
        print(snake_case[len(snake_case) - 1])
    elif snake_case[len(snake_case) - 1].isupper():
        print("_" + snake_case[len(snake_case) - 1].lower())


main()
