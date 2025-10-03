#!/usr/bin/env python

import csv
import numpy as np
from PIL import Image

# We want to calculate the brightness of every image
# and append it from views.csv to analysis.csv


def main():
    with open("views.csv") as views, open("analysis.csv", "w") as analysis:
        reader = csv.DictReader(views)
        writer = csv.DictWriter(analysis, fieldnames=reader.fieldnames + ["brightness"])
        # I've prepared the writer for retrieving the column names from the reader
        writer.writeheader()
        # And now adding them to analysis.csv and adding a new column called "brightness"

        for row in reader:
            row["brightness"] = round(calculate_brightness(f"{row['id']}.jpeg"), 2)
            # adds this new column to each row
            writer.writerow(row)  # and writes the whole readen row


def calculate_brightness(filename):
    with Image.open(filename) as image:
        brightness = np.mean(np.array(image.convert("L"))) / 255
    return brightness


if __name__ == "__main__":
    main()
