#!/usr/bin/env python

line = "     #as;dlfkjsad;lkfj"
if line[0] == " " and len(set(line.split("#")[0])) == 1:
    print(f"{line.split("#")[0]} starts with ' #'")
else:
    print("nope")
# list = "aaaaaaafaa"
# print(len(set(list)) == 1)
