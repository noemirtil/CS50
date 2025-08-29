#!/usr/bin/env python


def main():
    x, y, z = input("Epression: ").split(" ")

    match y:
        case "+":
            result = float(x) + float(z)
        case "-":
            result = float(x) - float(z)
        case "*":
            result = float(x) * float(z)
        case "/":
            result = float(x) / float(z)

    print(round(result, 1))


main()
