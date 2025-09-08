#!/usr/bin/env python

import random


def main():

    score = 0
    level = get_level()
    i = 0
    while i < 10:
        x = generate_integer(level)
        y = generate_integer(level)
        answer = int(input(f"{x} + {y} = "))
        if answer == x + y:
            score += 1
        else:
            print("EEE")
            j = 0
            while j < 2:
                answer = int(input(f"{x} + {y} = "))
                if answer == x + y:
                    score += 1
                    break
                else:
                    if j == 1:
                        print(f"{x} + {y} = {x + y}")
                    j += 1
        # print(f"Running score: {score}")
        i += 1
    print(f"Score: {score}")


def get_level():

    while True:
        level = input("Level: ")
        if level in ("1", "2", "3"):
            return int(level)
        else:
            continue
            # raise ValueError("Level should be 1, 2 or 3")


def generate_integer(level):

    if level == 1:
        return random.randint(0, 9)
    elif level == 2:
        return random.randint(10, 99)
    elif level == 3:
        return random.randint(100, 999)
    else:
        raise ValueError("Level should be 1, 2 or 3")


if __name__ == "__main__":
    main()
