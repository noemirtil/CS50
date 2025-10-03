#!/usr/bin/env python

import requests
import json
import re


def get_lyrics(artist, song):
    cleaned_artist = re.sub(r"\s\(.*\)", "", artist)
    cleaned_song = re.sub(r"\"|\s\(.*\)", "", song)
    longest_title_word = max(cleaned_song.split(" "), key=len)

    print(
        f"""Retrieving the lyrics of {song} by {artist}...
"""
    )

    file = requests.get(
        f"https://api.lyrics.ovh/v1/{cleaned_artist}/{cleaned_song}"
    ).json()

    # remove the [...] notes
    cleaned_file = re.sub(r"\[.*\]", "", file["lyrics"])
    # create a list of words
    split_file = re.split(r"[\s.,;:?()]", cleaned_file)
    # capitalize each word to solve case problems
    capitalized = list(map(str.capitalize, split_file))
    # create a dictionary of counted words
    counted_words = {word: capitalized.count(word) for word in capitalized}
    del counted_words[""]
    # created a sorted by values version of the dictionary
    sorted_words = dict(
        sorted(counted_words.items(), key=lambda key_val: key_val[1], reverse=True)
    )
    # create a list of the most significant quotes:
    quotes = re.findall(r"\n.*" + longest_title_word + r".*\n", cleaned_file, re.I)
    # print("These are the most significant words of this song:\n")
    for word in sorted_words:
        if sorted_words[word] > 4 and len(word) > 4:
            quotes.extend(re.findall(r"\n.*" + word + r".*\n", cleaned_file, re.I))
            # print(f"{word} is repeated {sorted_words[word]} times")

    print("These are the song's most significant phrases:\n")
    unique_quotes = list(set(quotes))
    unique_quotes.sort(key=lambda s: len(s))
    if len(unique_quotes) > 0:
        for quote in unique_quotes[:6]:
            quote_print = quote.replace("\n", "").capitalize()
            if quote_print[0] != "(":
                print(quote_print)
    print(
        f"""
======================================================
"""
    )


# url = input("url? ")
# print("\nRetrieving data...\n")

# if requests.get(url).status_code == 200:
#     print("Connection established...")

#     # Retrieve the song's lyrics
#     file = requests.get(url).json()
#     print(set(file["lyrics"].split("\s|.|,|;|:|?|(|)")))
#     # \s returns an "invalid escape sequence" warning ???
# else:
#     print("Sorry, the connection is down, try again later!")

# according to the Lyrics.ovh website it has two status codes 200 and 404. To briefly explain 200 error code means the request is successful (lyrics found) and 404 error code means (lyrics not found).

if __name__ == "__main__":
    get_lyrics()
