import os
import platform


def screen_clean():
    os_name = platform.system()
    if os_name == "Windows":
        os.system("cls")
    else:
        os.system("clear")  # for Mac and Linux
