#!/usr/bin/env python

import sys


class Jar:
    def __init__(self, capacity=12):
        self.capacity = capacity
        self.size = 0

    def __str__(self):
        return self._size * "🍪"

    def deposit(self, n):
        if (self._size + n) > self._capacity:
            raise ValueError("The jar is full!")
            # print("The jar is full!")
            # sys.exit(0)
        self._size += n

    def withdraw(self, n):
        if (self.size - n) < 0:
            raise ValueError("The jar is empty!")
            # print("The jar is empty!")
            # sys.exit(0)
        self._size -= n

    @property
    def capacity(self):
        return self._capacity

    @capacity.setter
    def capacity(self, capacity):
        if capacity < 0:
            raise ValueError("Not a non-negative capacity")
            # print("Not a non-negative capacity")
            # sys.exit(0)
        self._capacity = capacity

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, size):
        if size < 0:
            raise ValueError("Not a non-negative size")
            # print("Not a non-negative size")
            # sys.exit(0)
        self._size = size


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
