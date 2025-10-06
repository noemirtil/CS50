#!/usr/bin/env python

import json
import requests
import sys

import re
import wikipedia

# from albums import discography

from bs4 import BeautifulSoup
import requests as r


def get_charts(y):
    page = wikipedia.page("List_of_Billboard_Year-End_number-one_singles_and_albums")
    # create a BeautifulSoup Object
    soup = BeautifulSoup(
        page.html(),
        "html.parser",
    )
    # find the table we are looking for
    charts_table = soup.find("table", {"class": "wikitable"})
    # find all `tr` tags
    table_row = charts_table.find_all("tr")
    # create the dictionary
    years = {}
    # iterate over each table row to extract the <td> tag
    for col in table_row:
        html_col = col.find_all("td")
        if len(html_col) == 7:
            # create the year key/value(list) pair
            year = html_col[0].text.strip()[0:5]
            years[year] = {}
            i = 1
            while i < 7:
                if i in (1, 3, 5):
                    # select only the songs (and not the albums) to feed the dictionary
                    if matches := re.fullmatch(
                        r"(.+)\[\d+\](.+)", html_col[i].text.strip()
                    ):
                        years[year][f"song_{i}"] = matches.group(1)
                        years[year][f"artist_{i}"] = matches.group(2)
                    # elif matches := re.fullmatch(
                    #     r"(\".+\")\[\d\d\]\[\d\d\]\[self-published source\](.+)",
                    #     html_col[i].text.strip(),
                    # ):
                    #     years[year][f"song_{i}"] = matches.group(1)
                    #     years[year][f"artist_{i}"] = matches.group(2)
                    if not (f"song_{i}", f"artist_{i}") in years[year].keys():
                        years[year][f"song_{i}"] = "Not found 🙃"
                        # if not f"artist_{i}" in years[year].keys():
                        years[year][f"artist_{i}"] = "Not found 🙃"
                i += 1
    return years[y]


#     for col in table_row:
#         html_col = col.find_all("td")
#         if len(html_col) == 7:
#             years["year"] = html_col[0].text.strip()[0:5]
#             print(f"================ {years["year"]} TOP CHARTS =================")
#             i = 1
#             while i < 7:
#                 if i in (1, 3, 5):
#                     if matches := re.fullmatch(
#                         r"(.+)\[\d+\](.+)", html_col[i].text.strip()
#                     ):
#                         years[f"song_name_{i}"] = matches.group(1)
#                         years[f"artist_name_{i}"] = matches.group(2)
#                         print(
#                             f"{years[f"song_name_{i}"]}, by {years[f"artist_name_{i}"]}"
#                         )
#                 elif i in (2, 4, 6):
#                     if matches := re.fullmatch(
#                         r"(.+)\[\d+\](.+)", html_col[i].text.strip()
#                     ):
#                         years[f"album_name_{i}"] = matches.group(1)
#                         years[f"artist_name_{i}"] = matches.group(2)
#                         print(
#                             f"Artist: {years[f"artist_name_{i}"]} - Album: {years[f"album_name_{i}"]}"
#                         )
#                 i += 1
