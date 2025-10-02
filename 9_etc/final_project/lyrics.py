#!/usr/bin/env python

import requests
import json
import re


# def get_lyrics(artist, song):
#     get_lyrics(f"https://api.lyrics.ovh/v1/{artist}/{song}")


def get_lyrics():

    file = {
        #     "lyrics": "Sugar, ah honey honey\r\nYou are my candy girl\r\nAnd you've got me wanting you.\r\nHoney, ah sugar sugar\r\nYou are my candy girl\r\nAnd you've got me wanting you.\n\nI just can't believe the loveliness of loving you\n\n(I just can't believe it's true)\n\nI just can't believe the one to love this feeling to.\n\n(I just can't believe it's true)\n\nAh sugar, ah honey honey \n\nYou are my candy girl\n\nAnd you've got me wanting you.\n\nAh honey, ah sugar sugar\n\nYou are my candy girl\n\nAnd you've got me wanting you.\n\nWhen I kissed you, girl, I knew how sweet a kiss could be\n\n(I know how sweet a kiss can be)\n\nLike the summer sunshine pour your sweetness over me\n\n(Pour your sweetness over me)\n\nSugar, pour a little sugar on it honey,\n\nPour a little sugar on it baby\n\nI'm gonna make your life so sweet, yeah yeah yeah\n\nPour a little sugar on it oh yeah\n\nPour a little sugar on it honey,\n\nPour a little sugar on it baby\n\nI'm gonna make your life so sweet, yeah yeah yeah\n\nPour a little sugar on it honey,\n\nAh sugar, ah honey honey\n\nYou are my candy girl\n\nAnd you've got me wanting you.\n\nOh honey, honey, sugar sugar ..\n\nYou are my candy girl .."
        # }
        #     "lyrics": "Riders on the storm\r\nRiders on the storm\r\nInto this house we're born\r\nInto this world we're thrown\r\nLike a dog without a bone\r\nAn actor out alone\n\nRiders on the storm\n\n\n\nThere's a killer on the road\n\nHis brain is squirmin' like a toad\n\nTake a long holiday\n\nLet your children play\n\nIf you give this man a ride\n\nSweet memory will die\n\nKiller on the road, yeah\n\n\n\nGirl ya gotta love your man\n\nGirl ya gotta love your man\n\nTake him by the hand\n\nMake him understand\n\nThe world on you depends\n\nOur life will never end\n\nGotta love your man, yeah\n\n\n\nWow!\n\n\n\nRiders on the storm\n\nRiders on the storm\n\nInto this house we're born\n\nInto this world we're thrown\n\nLike a dog without a bone\n\nAn actor out alone\n\nRiders on the storm\n\n\n\nRiders on the storm\n\nRiders on the storm\n\nRiders on the storm\n\nRiders on the storm\n\nRiders on the storm"
        # }
        "lyrics": "Baby, ya yo me enteré, se nota cuando me ve'\r\nAhí donde no ha' llega'o sabe' que yo te llevaré\r\nY dime qué quiere' beber, e' que tú ere' mi bebé\r\n¿Y de nosotro' quién va a hablar? Si no nos dejamo' ver\r\nY a vece' e' Dolce, a vece' Bulgari\n\nCuando te lo quito despué' de lo' partie'\n\nLas copa' de vino, las libra' de mari\n\nTú estás bien suelta, yo de safari\n\nTú muevе' el culo fenomenal\n\nPa' yo dеvorarte como animal\n\nSi no te ha' venío', yo te vo'a esperar\n\nEn mi cama y lo vo'a celebrar\n\n\n\nBaby, a ti no me opongo\n\nY siempre te lo pongo\n\nY si tú me tira', vamo' a nadar en lo hondo\n\nSi e' por mí te lo pongo\n\nDe septiembre hasta agosto\n\nA mí sin cojone' a lo que digan tu' amiga'\n\n[Estribillo: Bad Bunny & Jhay Cortez]\n\nYa yo me enteré, se nota cuando me ve'\n\nAhí donde no ha' llega'o sabe' que yo te llevaré\n\nY dime qué quiere' beber, e' que tú ere' mi bebé\n\n¿Y de nosotro' quién va a hablar? Si no nos dejamo' ver (¿Me sigue'?)\n\n\n\nMami, me tiene' juquea'o, sí\n\nSi fuera' la Uru', me tuviese' parquea'o\n\nDando vuelta' por Condado, contigo siempre arrebata'o\n\nTú no ere' mi señora, pero\n\nToma cinco mil, gástalo en Sephora\n\nLouis Vuitton, ya no compra en Pandora\n\nComo piercing, a los hombre' perfora, eh-eh-eh\n\n\n\nHace tiempo le rompieron el cora (El cora)\n\nEstudiosa, puesta pa' ser doctora (Doctora)\n\nPero (Pero), le gustan los títere' wheeliando motora' (Motora')\n\nYo estoy pa' ti las veinticuatro hora'\n\n\n\nBaby, a ti no me opongo\n\nY siempre te lo pongo (Siempre te lo pongo)\n\nY si tú me tira', vamo' a nadar en lo hondo (Nadar en lo hondo)\n\nSi es por mí te lo pongo\n\nDe septiembre hasta agosto\n\nY a mí sin cojone' lo que digan tu' amiga'\n\n\n\nYa yo me enteré, se nota cuando me ve'\n\nAhí donde no ha' llega'o sabe' que yo te llevaré\n\nY dime qué quiere' beber, e' que tú ere' mi bebé\n\n¿Y de nosotro' quién va a hablar? Si no nos dejamo' ver\n\n\n\nY a vece' e' Dolce, a vece' Bulgari\n\nCuando te lo quito despué' de lo partie'\n\nLa' copa' de vino, las libra' de mari\n\nTú estás bien suelta, yo de safari\n\nTú mueve' el culo fenomenal\n\nPa' yo devorarte como animal\n\nSi no te ha' venío', yo te vo'a esperar\n\nEn mi cama y lo vo'a celebrar"
    }
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
    for word in sorted_words:
        print(f"{word}: {sorted_words[word]} times")


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


if __name__ == "__main__":
    get_lyrics()
