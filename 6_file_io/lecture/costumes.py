#!/usr/bin/env python

import sys
from PIL import Image

images = []

for arg in sys.argv[1:]:
    image = Image.open(arg)
    images.append(image)
# this loop's only purpose is to append each image to the list

images[0].save(
    "costumes.gif", save_all=True, append_images=[images[1]], duration=200, loop=0
)
# the pillow library takes care of doing the opening,
# the closing and the saving of the image just by calling "save"
