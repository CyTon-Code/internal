from typing import IO


class FileDidNotClose(Exception):
    # The file didn't close
    def __init__(self):
        pass


class ErrorClearFile(Exception):
    def __init__(self):
        pass


def file_read(file: IO) -> bool or None:
    try:  # The file is read:
        file.read()
        return False  # Answer: The file is there, and it has been read.

    except:  # file not read:
        return None  # Answer: The file is present, but not readable.


def file_close(file: IO, commit: str) -> None or Exception:
    try:  # Closes the file:
        file.close()

    except:  # The file didn't close:
        print(f"error: {commit}")
        raise FileDidNotClose  # Answer: The file won't close! We
        # throw in the program: "Exception".
