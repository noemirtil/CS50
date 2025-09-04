def main():
    original = input("Please write something with emoticons: ")
    print(convert(original))


def convert(string):
    return string.replace(":)", "🙂").replace(":(", "🙁")


main()
