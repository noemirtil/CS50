#!/usr/bin/env python

import re
import sys


def main():
    print(parse(input("HTML: ")))


def parse(s):
    if match := re.search(r"\"https?://(?:www.)?youtube.com/embed/(.+?)\"", s):
        return f"https://youtu.be/{match.group(1)}"


if __name__ == "__main__":
    main()
