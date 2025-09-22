#!/usr/bin/env python


class Package:
    def __init__(self, number, sender, recipient, weight):
        # Here information is encapsulated using instance variables:
        self.number = number
        self.sender = sender
        self.recipient = recipient
        self.weight = weight

    # Here is encapsulated a special dunder method
    def __str__(self):
        return (
            f"Package {self.number}: {self.sender} to {self.recipient}, {self.weight}kg"
        )

    # Here is encapsulated an instance method
    def calculate_cost(self, cost_per_kg):
        return self.weight * cost_per_kg


def main():
    packages = [
        # Here number gets assigned as an instance variable within this instance of the class Package:
        Package(number=13, sender="Alice", recipient="Bob", weight=10),
        Package(number=38, sender="Bob", recipient="Charlie", weight=5),
    ]
    for package in packages:
        print(f"{package} costs ${package.calculate_cost(cost_per_kg=2)}")


if __name__ == "__main__":
    main()
