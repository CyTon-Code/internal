"""
    The module works only through import.
    Via os.system or return (RUN) - doesn't work.
"""

import os
from internal.check_open_file import check_open_file
from additional.get_name_from_link import get_name_from_link

if __name__ == "__main__":  # If not imported, I exit is the module:
    print("I am is Module!!! Bye Bye!!!")
    exit()  # Answer: I'm leaving, I'm a module.


def move_file(link: str, path="work/moving_a_file.py"):
    # If the names are the same, but the addresses are different, you can move:
    if link == path or not get_name_from_link(link) == get_name_from_link(path):
        return True

    else:  # Перемещаем и переименовываем файл:
        if check_open_file(link):  # if (os.path.exists(link)):
            os.replace(link, path)  # cut
            return False

        else:  # There is no file, so there is no point in moving:
            return None
