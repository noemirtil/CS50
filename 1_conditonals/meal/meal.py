#!/usr/bin/env python


def main():
    time = input("What time is it? ")

    if time.endswith(".m."):
        prefix, sufix = time.split(" ")

        if sufix == ("a.m."):
            if 7 <= convert(prefix) <= 8:
                print("breakfast time")
            elif 12 <= convert(prefix) < 13:
                print("lunch time")
            else:
                pass

        elif sufix == ("p.m."):
            if convert(prefix) == 1:
                print("lunch time")
            elif 6 <= convert(prefix) <= 7:
                print("dinner time")
            else:
                pass

        else:
            pass

    else:
        if 7 <= convert(time) <= 8:
            print("breakfast time")
        elif 12 <= convert(time) <= 13:
            print("lunch time")
        elif 18 <= convert(time) <= 19:
            print("dinner time")
        else:
            pass


def convert(time):
    hours, minutes = time.split(":")
    return float(minutes) / 60 + float(hours)


if __name__ == "__main__":
    main()
