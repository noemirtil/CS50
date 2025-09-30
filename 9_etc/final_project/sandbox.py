#!/usr/bin/env python


# def generate():
#     for i in range(3):
#         yield i


# gen = generate()
# print(next(gen))
# print(next(gen))


# a = [1, 2, 3]
# b = (4, 5, 6)
# c = zip(a, b)
# print(list(c))

my_list = [1, 1, 2, 3, 2, 2, 4, 5, 6, 2, 1]
my_final_list = set(my_list)
print(my_final_list)
print(list(my_final_list))
