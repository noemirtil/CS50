#!/usr/bin/env python

import requests
import json
import re
import lyricsgenius


def get_lyrics(artist, song):
    cleaned_artist = re.sub(r"\s\(.*\)|/.*", "", artist).strip()
    cleaned_song = re.sub(r"\"|\s\(.*\)|[\(\)]|/.*", "", song).strip()
    longest_title_word = max(cleaned_song.split(" "), key=len)

    # my personal token
    tokenized = lyricsgenius.Genius(
        "w7Y1kofFOGXkztFMC5gC4SaRzxm24pxZraUU8n902tbu9opjgdkQlh8WHP5BDylB"
    )
    # retrieving the song's lyrics
    try:
        file = tokenized.search_song(cleaned_song, cleaned_artist)
        if file != None:
            # remove the [...] notes
            cleaned_file = re.sub(r"\[.*\]|\(.*\)|\(\n|\n\)", "", file.lyrics)
            # create a list of words
            split_file = re.split(r"[\s.,;:?()]", cleaned_file)
            # capitalize each word to solve case problems
            capitalized = list(map(str.capitalize, split_file))
            # create a dictionary of counted words
            counted_words = {word: capitalized.count(word) for word in capitalized}
            del counted_words[""]
            # created a sorted by values version of the dictionary
            sorted_words = dict(
                sorted(
                    counted_words.items(), key=lambda key_val: key_val[1], reverse=True
                )
            )
            # create a list of the quotes containing longest_title_word
            quotes = re.findall(
                r"\n.*" + longest_title_word + r".*\n", cleaned_file, re.I
            )
            # extend quotes list to the most repeated words
            for word in sorted_words:
                if sorted_words[word] > 4 and len(word) > 5:
                    quotes.extend(
                        re.findall(r"\n.*" + word + r".*\n", cleaned_file, re.I)
                    )
            # remove duplicates
            unique_quotes = list(
                set(map(str.strip, [s.replace('"', "") for s in quotes]))
            )
            unique_quotes.sort(key=lambda s: len(s))
            print("")
            if len(unique_quotes) > 0:
                for quote in unique_quotes[:4]:
                    quote_print = quote.replace("\n", "").capitalize()
                    if quote_print[0] != "(":
                        print(quote_print)
            else:
                print("Sorry, this song lacks lyrics 🙃")
            print(
                f"""
======================================================
            """
            )
        else:
            print("Sorry 🙃\n")

    except requests.exceptions.RequestException:
        print("Sorry, this song was not found 🙃\n")


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
