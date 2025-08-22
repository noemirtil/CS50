def main():
    name = input("What's your name? ")
    hello(name)
# By convention, the main purpose of a script is defined in the "main()" function at the top of the file
def hello(to="world"):
    print("hello,", to)
# Then, it is followed by the custom functions it will have to call
main()
#and finally, the main() is called