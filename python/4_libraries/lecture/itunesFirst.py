#!/usr/bin/env python

import json
import requests
import sys


def main():
    if len(sys.argv) != 2:
        sys.exit()

    response = requests.get(
        "https://itunes.apple.com/search?entity=song&limit=1&term=" + sys.argv[1]
    )
    print(json.dumps(response.json(), indent=2))


if __name__ == "__main__":
    main()
