#!/usr/bin/python3
"""
function that appends a string at the end of a text file
and returns the number of characters added.
"""


def append_write(filename="", text=""):
    """Append to file with text
    args:
        filename: add to this object
        text: string to append
    return:
        number of characters added
    """

    with open(filename, mode="a", encoding="utf-8") as f:
        if f.write(text):
            return len(text)
