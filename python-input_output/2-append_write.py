#!/usr/bin/python3
"""
function that appends a string at the end of a text file
and returns the number of characters added
"""


def append_write(filename="", text=""):
    """ function that appends a string at the end of a text file"""

    with open(filename, "a", encoding="utf-8") as f:
        return file.write(text)
