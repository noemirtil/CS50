#!/usr/bin/env python

import json
import requests
import sys


def discography(search):
    # Retrieve the artist search data from iTunes
    search_data = requests.get(
        "https://itunes.apple.com/search?entity=album&limit=201&term=" + search
    ).json()

    # Getting every artist id corresponding to the search and eliminate duplicates with a set
    ids = set()
    for result in search_data["results"]:
        ids.add(result["artistId"])

    # Create a list of dictionaries containing an empty list of albums for each id
    albums_by_id = []
    for id in ids:
        albums_by_id.append({"id": id, "albums": []})

    # Append every album and date to a new dictionary for each id into the empty lists of each dictionary
    for dic in albums_by_id:
        for result in search_data["results"]:
            if dic["id"] == result["artistId"]:
                dic["albums"].append(
                    {
                        "release_name": result["collectionName"],
                        "release_date": result["releaseDate"],
                        "track_count": result["trackCount"],
                        "release_id": result["collectionId"],
                    }
                )
                # Add the number of albums for every id
                dic["count"] = len(dic["albums"])

    # Select one main artist according to the highest number of albums
    main_artist = sorted(albums_by_id, key=lambda d: d["count"], reverse=True)[0]

    # Get main artist's name
    for result in search_data["results"]:
        if main_artist["id"] == result["artistId"]:
            name = result["artistName"]

    # Display main artist's data
    print(
        f"""
===========================================
{name}: {main_artist['count']} albums discography:
==========================================="""
    )

    # Display the list of its albums
    for album in sorted(main_artist["albums"], key=lambda s: s["release_date"]):
        # Retrieve each album's own data from iTunes
        album_data = requests.get(
            "https://itunes.apple.com/lookup?entity=song&id=" + str(album["release_id"])
        ).json()

        # Calculate the average duration of each album's tracks
        length = 0
        for result in album_data["results"]:
            if result["wrapperType"] == "track":
                if result.get("trackTimeMillis") != None:
                    length += int(result["trackTimeMillis"])
        millis = length / album["track_count"]
        seconds = millis / 1000 % 60
        minutes = millis / 60000

        print(
            f"""{album["release_date"][:4]}: {album["release_name"]}
{album["track_count"]} songs with an average of {minutes:.0f}min {seconds:.0f}sec per song
-------------------------------------------"""
        )
