#!/usr/bin/env python

import random


def main():

    while True:

        try:
            level = int(input("Level: "))
        except (ValueError, TypeError):
            continue
        except EOFError:
            break
        if level < 1:
            continue
        else:
            rand = random.randint(1, level)
            while True:
                try:
                    guess = int(input("Guess: "))
                except (ValueError, TypeError):
                    continue
                except EOFError:
                    break
                if guess < 1:
                    continue
                else:
                    if guess < rand:
                        print("Too small!")
                        continue
                    if guess > rand:
                        print("Too large!")
                        continue
                    if guess == rand:
                        print("Just right!")
                        break
            break


if __name__ == "__main__":
    main()
