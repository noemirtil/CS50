#!/usr/bin/env python

import sys
import requests


def main():

    try:
        factor = float(sys.argv[1])
    except:
        if len(sys.argv) == 2:
            sys.exit("Command-line argument is not a number")
        else:
            sys.exit("Missing command-line argument")
    else:
        try:
            response = requests.get(
                "https://rest.coincap.io/v3/assets/bitcoin?apiKey=f2da0b224dd16893b151c15caa9d37b36f5dda7addf41bda4bc2947990e99184"
            )
            response.raise_for_status()
            # print(response)
            currency = float(response.json()["data"]["priceUsd"])
            print(f"${(currency * factor):,.4f}")
        except requests.HTTPError:
            print("Couldn't complete request!")
            return


if __name__ == "__main__":
    main()
