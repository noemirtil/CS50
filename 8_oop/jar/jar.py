#!/usr/bin/env python

import sys


class Jar:
    def __init__(self, quantity=0, capacity=12):
        self.capacity = capacity
        self.quantity = quantity

    def __str__(self):
        return self.quantity * "🍪"

    def deposit(self, n):
        if (self.quantity + n) > self.capacity:
            raise ValueError("The jar is full!")
            # print("The jar is full!")
            # sys.exit(0)
        self.quantity += n

    def withdraw(self, n):
        if (self.quantity - n) < 0:
            raise ValueError("The jar is empty!")
            # print("The jar is empty!")
            # sys.exit(0)
        self.quantity -= n

    # Getter:
    @property
    def capacity(self):
        return self._capacity

    # Setter:
    @capacity.setter
    def capacity(self, capacity):
        if capacity < 0:
            raise ValueError("Not a non-negative capacity")
            # print("Not a non-negative capacity")
            # sys.exit(0)
        self._capacity = capacity

    # Getter:
    @property
    def size(self):
        return self._quantity

    # Setter:
    @size.setter
    def size(self, quantity):
        if quantity < 0:
            raise ValueError("Not a non-negative quantity")
            # print("Not a non-negative quantity")
            # sys.exit(0)
        self._quantity = quantity


def main():
    unique_jar = Jar()
    add = int(input("How many cookies to add? "))
    unique_jar.deposit(add)
    print(unique_jar)
    eat = int(input("How many cookies to eat? "))
    unique_jar.withdraw(eat)
    print(unique_jar)


if __name__ == "__main__":
    main()
