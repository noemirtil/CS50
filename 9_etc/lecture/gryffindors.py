#!/usr/bin/env python

students = ["Hermione", "Harry", "Ron"]
# three ways to print the same:
# 0 Hermione 1 Harry 2 Ron

i = 0
for item in students:
    print(i, students[i], end=" ")
    i += 1

for i in range(len(students)):
    print(i, students[i], end=" ")

for i, student in enumerate(students):
    print(i, student, end=" ")

# gryffindors = [{"name": student, "house": "Gryffindor"} for student in students]

# gryffindors = {student: "Gryffindor" for student in students}

# print(gryffindors)


# students = [
#     {"name": "Hermione", "house": "Gryffindor"},
#     {"name": "Harry", "house": "Gryffindor"},
#     {"name": "Ron", "house": "Gryffindor"},
#     {"name": "Draco", "house": "Slytherin"},
#     {"name": "Padma", "house": "Ravenclaw"},
# ]


# def is_gryffindor(s):
#     return s["house"] == "Gryffindor"

# gryffindors = filter(is_gryffindor, students)

# for gryffindor in sorted(gryffindors, key=lambda s: s["name"]):
#     print(gryffindor["name"])

# print(*gryffindors)

# students = [
#     {"name": "Hermione", "house": "Gryffindor"},
#     {"name": "Harry", "house": "Gryffindor"},
#     {"name": "Ron", "house": "Gryffindor"},
#     {"name": "Draco", "house": "Slytherin"},
#     {"name": "Padma", "house": "Ravenclaw"},
# ]

# for student in sorted(students, key=lambda s: s["name"]):
#     print(student["name"], end=" ")

# print(*gryffindors)
