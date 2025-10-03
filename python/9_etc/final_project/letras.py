#!/usr/bin/env python

import json
import requests
import sys

import re

# from albums import discography

from bs4 import BeautifulSoup
import requests as r


def get_genius():
    page = "https://www.letras.com/earth-wind-and-fire/12114/"
    # create a BeautifulSoup Object
    soup = BeautifulSoup(
        page.html(),
        "html.parser",
    )
    # find the table we are looking for
    letras = soup.find("div", {"class": "lyric-original"})
    print(letras)


if __name__ == "__main__":
    get_genius()
