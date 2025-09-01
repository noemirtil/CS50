#!/usr/bin/env python

words = ["hey", "you", "how", "hey", "are", "doing", "hey", "you"]


def main():

    # counts = {}
    # for word in words:
    #     if word in counts:
    #         counts[word] += 1
    #     else:
    #         counts[word] = 1

    counts = {word: words.count(word) for word in words}

    print(counts)


main()
