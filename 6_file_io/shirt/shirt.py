#!/usr/bin/env python

import sys
import os.path
from PIL import Image
from PIL import ImageOps


def main():
    check_arguments()
    # print(sys.argv[1:3])
    with Image.open(sys.argv[1]) as before, Image.open("shirt.png") as shirt:
        # print(f"{sys.argv[1]} is {before.size}")
        # print(f"'shirt.png' is {shirt.size}")
        before = ImageOps.fit(image=before, size=[600, 600])
        before.paste(im=shirt, mask=shirt)
        before.save(sys.argv[2])
    # with Image.open(sys.argv[2]) as after:
    # print(f"{sys.argv[2]} is {after.size}")


def check_arguments():
    valid_suffixes = (".jpg", ".jpeg", ".png")
    passed_suffix1 = os.path.splitext(sys.argv[1])
    passed_suffix2 = os.path.splitext(sys.argv[2])
    if len(sys.argv) < 3:
        print("Too few command-line arguments")
    elif len(sys.argv) > 3:
        print("Too many command-line arguments")
    elif not passed_suffix1[-1] in valid_suffixes:
        print("Invalid input")
    elif not passed_suffix2[-1] in valid_suffixes:
        print("Invalid output")
    elif passed_suffix1[-1] != passed_suffix2[-1]:
        print("Input and output have different extensions")
    elif not os.path.exists(sys.argv[1]):
        print(f"Could not read {sys.argv[1]}")
    else:
        return
    sys.exit(1)


if __name__ == "__main__":
    main()
