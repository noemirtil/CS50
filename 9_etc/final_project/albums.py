#!/usr/bin/env python

import json
import requests
import sys


def main():
    if len(sys.argv) != 2:
        sys.exit()

    response = requests.get(
        "https://itunes.apple.com/search?entity=album&limit=201&term=" + sys.argv[1]
    )

    data = response.json()

    ids = set()
    for result in data["results"]:
        ids.add(result["artistId"])
    albums_by_id = []
    for id in ids:
        albums_by_id.append({"id": id, "albums": []})

    for _ in albums_by_id:
        for result in data["results"]:
            if _["id"] == result["artistId"]:
                _["albums"].append(result["collectionName"])

    for album in albums_by_id:
        print(album)


if __name__ == "__main__":
    main()
