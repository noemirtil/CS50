#!/usr/bin/env python

import re
import json

# def generate():
#     for i in range(3):
#         yield i


# gen = generate()
# print(next(gen))
# print(next(gen))


# a = [1, 2, 3]
# b = (4, 5, 6)
# c = zip(a, b)
# print(list(c))

# my_list = [1, 1, 2, 3, 2, 2, 4, 5, 6, 2, 1]
# my_final_list = set(my_list)
# print(my_final_list)
# print(list(my_final_list))

# -------------------------------------------

# cleaned_file = "Moment of honesty,\r\nSomeones gotta take the lead tonight\r\nWhose it gonna be?\r\nI'm gonna sit right here and tell you all that comes to me\r\nIf you have something to say\r\nYou should say it right now\n\n(You should say it right now)\n\n\n\nYou give me a feeling that I never felt before\n\nAnd I deserve it, I know I deserve it\n\nIts become something that's impossible to ignore\n\nAnd I can't take it\n\nI was wondering maybe\n\nCould I make you my baby\n\nIf we do the unthinkable will it make us look crazy\n\nIf you ask me I'm ready (I'm ready)\n\nIf you ask me I'm ready (I'm ready)\n\n\n\nI know you said to me\n\nThis is exactly how it should feel when its meant to be\n\nTime is only wasting so why wait for eventually\n\nIf we gonna do something about it\n\nWe should do it right now\n\n(We should do it right now)\n\n\n\nYou give me a feeling that I never felt before\n\nAnd I deserve it, I know I deserve it\n\nIts becoming something that's impossible to ignore\n\nIts what we make it\n\n\n\nI was wondering maybe\n\nCould I make you my baby\n\nIf we do the unthinkable\n\nWill it make us look crazy\n\nOr would it be so beautiful\n\nEither way I'm sayin\n\nIf you ask me I'm ready (I'm ready)\n\nIf you ask me I'm ready (I'm ready)\n\n\n\nSayin\n\nwhy give up before we try\n\nFeel the lows before the highs\n\nClip our wings before we fly away (fly away)\n\nI can't say I came prepared\n\nI'm suspended in the air\n\nWon't u come be in the sky with me"
# song = "Un-Thinkable (I'm Ready)"
# cleaned_song = re.sub(r"\"|\s\(.*\)", "", song)
# longest_title_word = max(cleaned_song.split(" "), key=len)
# print(f"longest_title_word: {longest_title_word}")

# # print the most important quotes
# quotes = re.findall(r"\n.*" + longest_title_word + r".*\n", cleaned_file, re.I)
# for quote in quotes:
#     print(quote.replace("\n", ""))

# ---------------------------------------------

cleaned_artist = "Alicia Keys"
cleaned_song = "Un-Thinkable"
longest_title_word = max(cleaned_song.split(" "), key=len)

file = "Moment of honesty,\r\nSomeones gotta take the lead tonight\r\nWhose it gonna be?\r\nI'm gonna sit right here and tell you all that comes to me\r\nIf you have something to say\r\nYou should say it right now\n\n(You should say it right now)\n\n\n\nYou give me a feeling that I never felt before\n\nAnd I deserve it, I know I deserve it\n\nIts become something that's impossible to ignore\n\nAnd I can't take it\n\nI was wondering maybe\n\nCould I make you my baby\n\nIf we do the unthinkable will it make us look crazy\n\nIf you ask me I'm ready (I'm ready)\n\nIf you ask me I'm ready (I'm ready)\n\n\n\nI know you said to me\n\nThis is exactly how it should feel when its meant to be\n\nTime is only wasting so why wait for eventually\n\nIf we gonna do something about it\n\nWe should do it right now\n\n(We should do it right now)\n\n\n\nYou give me a feeling that I never felt before\n\nAnd I deserve it, I know I deserve it\n\nIts becoming something that's impossible to ignore\n\nIts what we make it\n\n\n\nI was wondering maybe\n\nCould I make you my baby\n\nIf we do the unthinkable\n\nWill it make us look crazy\n\nOr would it be so beautiful\n\nEither way I'm sayin\n\nIf you ask me I'm ready (I'm ready)\n\nIf you ask me I'm ready (I'm ready)\n\n\n\nSayin\n\nwhy give up before we try\n\nFeel the lows before the highs\n\nClip our wings before we fly away (fly away)\n\nI can't say I came prepared\n\nI'm suspended in the air\n\nWon't u come be in the sky with me"

# remove the [...] notes
cleaned_file = re.sub(r"\[.*\]", "", file)
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

print("These are the most significant phrases of this song:\n")
unique_quotes = list(set(quotes))
unique_quotes.sort(key=lambda s: len(s))
if len(unique_quotes) > 0:
    for quote in unique_quotes[:10]:
        quote_print = quote.replace("\n", "").capitalize()
        if quote_print[0] != "(":
            print(quote_print)
