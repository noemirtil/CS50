#!/usr/bin/env python

import json
import requests
import sys
from albums import discography
from charts import get_charts


def main():
    year = input("Please type a year between 2006 and 2024: ")
    print(get_charts(year))
    # search = input("Please type the name of a music artist: ").strip()
    # discography(search)


if __name__ == "__main__":
    main()
