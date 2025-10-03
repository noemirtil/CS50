#!/usr/bin/env python


class Vault:
    # these currencies refer to some of thoses availables in Gringott's vault:
    def __init__(self, galleons=0, sickles=0, knuts=0):
        self.galleons = galleons
        self.sickles = sickles
        self.knuts = knuts

    def __str__(self):
        return f"{self.galleons} Galleons, {self.sickles} Sickles, {self.knuts} Knuts"

    def __add__(self, other):
        galleons = self.galleons + other.galleons
        sickles = self.sickles + other.sickles
        knuts = self.knuts + other.knuts
        return Vault(galleons, sickles, knuts)


potter = Vault(100, 50, 25)
print(potter)

weasley = Vault(25, 50, 100)
print(weasley)

# Hereafter, the + sign will be able to operate thanks to the previous definition of
# the __add__(self, other) method, inside of which I have taght python what it means to add two vaults together
total = potter + weasley
print(total)
