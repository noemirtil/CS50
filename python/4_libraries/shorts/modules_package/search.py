#!/usr/bin/env python

# No use thanks to the creation of my own museum package:
# from artists import get_artists
# from artwork import get_artworks

from museum.artists import get_artists
from museum.artwork import get_artworks


def main():
    artist = input("Artist: ")
    artists = get_artists(query=artist, limit=5)
    for artist in artists:
        print(f"* {artist}")

    artwork = input("Artwork: ")
    artworks = get_artworks(query=artwork, limit=5)
    for artwork in artworks:
        print(f"* {artwork}")


if __name__ == "__main__":
    main()
