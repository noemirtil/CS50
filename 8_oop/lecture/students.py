#!/usr/bin/env python


class Student:
    def __init__(self, name, house):
        self.name = name
        self.house = house

    def __str__(self):
        return f"{self.name} from {self.house}"

    # Getter:
    @property
    def name(self):
        # always one only argument
        return self._name
        # the _ is a convention to prevent using the same variable name as declared in __init__ function

    # Setter:
    @name.setter
    def name(self, name):
        # always two arguments
        if not name:
            raise ValueError("Missing name")
        self._name = name
        # the _ is a convention to prevent using the same variable name as declared in __init__ function.

    @property
    def house(self):
        return self._house

    @house.setter
    def house(self, house):
        if house not in ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]:
            raise ValueError("Invalid house")
        self._house = house


def main():
    student = get_student()
    # student.name = "Lalalala"
    # student.house = "Lilililili"
    # Thanks to the implementation of the setter and getter, this kind of malicious lines of code will generate the ValueErrors!
    # student._house = "Lilililili"
    # Unfortunately, doing the same to the underscored variable would override the protections, that's why, in the world of python, this underscore means "private", you just should never touch it (Honor system). This might also be indicated with two underscores
    print(student)


def get_student():
    name = input("Name: ")
    house = input("House: ")
    return Student(name, house)


if __name__ == "__main__":
    main()
