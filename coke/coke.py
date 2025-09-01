#!/usr/bin/env python


def main():
    due = 50
    while due > 0:
        print(f"Amount due: {due}")
        inserted = int(input("Insert coin: "))
        if (inserted == 25) or (inserted == 10) or (inserted == 5):
            due -= inserted
        else:
            pass
    print(f"Change owed: {due * (-1)}")


main()
