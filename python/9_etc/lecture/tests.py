#!/usr/bin/env python

import os


round = 0


def read(directory):
    global round
    if directory == "":
        directory = f"../"
    for item in os.listdir(directory):
        # if os.path.isfile(directory + item) and item == os.listdir(directory)[-1]:
        #     print(f" └─ {item}")
        if os.path.isfile(directory + item):
            print(f"{round}{round * "│ "}├─{item}")
        if os.path.isdir(directory + item):
            print(f"{round}{round * "├─"}{item}/")
            round += 1
            read(f"{directory}{item}/")


# Implement arguments...
# read("/Users/noemi/Dropbox/DevWork/repos/github/noemirtil/CS50/9_etc/")
read("")

"""
Follow this model:

the-corner-shop/
├── app/
│ ├── models/
│ │ ├── product.py
│ │ ├── user.py
│ │ └── order.py
│ ├── controllers/
│ │ ├── auth_controller.py
│ │ ├── product_controller.py
│ │ └── order_controller.py
│ ├── views/
│ │ └── templates/
│ ├── static/
│ │ └── css/
│ └── main.py
├── database/
│ └── corner_shop.db
├── requirements.txt
└── README.md


"""
