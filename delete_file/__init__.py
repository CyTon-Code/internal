"""
    The module works only through import.
    Via os.system or return (RUN) - doesn't work.
"""

from internal.check_open_file import check_open_file
import os

if __name__ == "__main__":  # If not imported, I exit is the module:
    print("I am is Module!!! Bye Bye!!!")
    exit()  # Answer: I'm leaving, I'm a module.


def delete_file(link: str) -> bool or None:  # Delete existing file:
    if check_open_file(link):  # If the file does not exist:
        return False  # Answer: The file to be deleted does not exist.

    try:  # Delete the file:
        os.remove(link)
        return True  # Answer: The file existed and was deleted.

    except:  # Delete failed:
        return None  # Answer: The file exists but has not been deleted.
