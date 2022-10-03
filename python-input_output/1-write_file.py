#!/usr/bin/python3
"""
Module 1-write_file
function that writes a string to a text file and
returns the number of char written
"""


def write_file(filename="", text=""):
    """function that writes a string to a text file"""

    with open(filename, mode="w", encoding="utf-8") as f:
        return f.write(text)
