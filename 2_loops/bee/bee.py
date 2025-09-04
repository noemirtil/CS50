#!/usr/bin/env python

WORDS = {"PAIR": 4, "HAIR": 4, "CHAIR": 5}


def main():
    print("Welcome to Spelling Bee!")
    print("Your letters are: A I P C R H G")

    while len(WORDS) > 0:
        print(f"{len(WORDS)} left!")
        guess = input("Guess a word: ")

        if guess == "GRAPHIC":
            WORDS.clear()
            print("YOU WON - GAME OVER!!!")
        elif guess in WORDS.keys():
            points = WORDS.pop(guess)
            # points retrieves the value of the popped pair,
            # in order to serve it in the next line:
            print(f"Good job! You scored {points} points.")

    print("That's it, congrats!")


main()
