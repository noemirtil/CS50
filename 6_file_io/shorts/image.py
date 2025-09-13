#!/usr/bin/env python

from PIL import Image
from PIL import ImageFilter


def main():
    with Image.open("img/in.jpeg") as img:
        # open is a method of the Image Class to open the in.jpeg file
        # file is automatically closed as soon as we exit the indentation
        print(img.size)
        print(img.format)
        img = img.rotate(180)
        img = img.filter(ImageFilter.FIND_EDGES)
        img = img.filter(ImageFilter.BLUR)
        img.save("img/out.jpeg")


if __name__ == "__main__":
    main()
