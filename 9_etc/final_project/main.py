#!/usr/bin/env python

import json
import requests
import sys
from albums import discography
from charts import get_charts
from helpers import screen_clean
from lyrics import get_lyrics


def main():
    year = input("Please type a year between 1946 and 2024: ")
    print("\nRetrieving data...\n")
    year_charts = get_charts(year)

    screen_clean()
    print(
        f"""



================== {year} TOP SONGS ==================

       Pop charts:
  1️⃣   {year_charts['song_1']}
       by {year_charts['artist_1']}

       R&B/Soul/Hip-Hop charts:
  2️⃣   {year_charts['song_3']}
       by {year_charts['artist_3']}

       Country charts:
  3️⃣   {year_charts['song_5']}
       by {year_charts['artist_5']}

"""
    )
    choice = input(
        """Which one of these songs calls your attention?
(type 1, 2, or 3): """
    )

    match choice:
        case "1":
            get_lyrics(artist=year_charts["artist_1"], song=year_charts["song_1"])
        case "2":
            get_lyrics(artist=year_charts["artist_3"], song=year_charts["song_3"])
        case "3":
            get_lyrics(artist=year_charts["artist_5"], song=year_charts["song_5"])
            # get_lyrics(f"https://api.lyrics.ovh/v1/{year_charts['artist_5']}/{year_charts['song_5']}")


def interface():
    try:
        main()
    except EOFError:
        sys.exit(0)


if __name__ == "__main__":
    interface()
