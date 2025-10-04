#!/usr/bin/env python

import json
import requests
import sys
from albums import discography
from charts import get_charts
from helpers import screen_clean
from lyrics import get_lyrics


def main():
    screen_clean()
    year = input(
        """

Please type a year between 1946 and 2024:

=> """
    )
    try:
        if 1945 < int(year) < 2025:
            print("\nRetrieving data...\n")
            year_charts = get_charts(year)

            screen_clean()
            print(
                f"""

================== {year} TOP SONGS ==================

Pop charts:
        {year_charts['song_1']}
        by {year_charts['artist_1']}

R&B/Soul/Hip-Hop charts:
        {year_charts['song_3']}
        by {year_charts['artist_3']}

Country charts:
        {year_charts['song_5']}
        by {year_charts['artist_5']}


Here are some significant quotes from these songs:
"""
            )

            i = 1
            while i < 7:
                if (
                    i in (1, 3, 5)
                    and year_charts[f"artist_{i}"] != "Not found 🙃"
                    and year_charts[f"song_{i}"] != "Not found 🙃"
                ):
                    try:
                        get_lyrics(
                            artist=year_charts[f"artist_{i}"],
                            song=year_charts[f"song_{i}"],
                        )
                    except KeyError:
                        print(
                            f"\nCouldn't retrieve some {year} {i} data, please try again 🙃\n"
                        )
                i += 1

        else:
            main()

    except ValueError:
        main()


def interface():
    try:
        main()
    except EOFError:
        sys.exit(0)


if __name__ == "__main__":
    interface()
