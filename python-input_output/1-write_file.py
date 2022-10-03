#!/usr/bin/python3
"""
Module 1-number_of_lines
function that writes a string to a text file and
returns the number of char written
"""


def number_of_lines(filename=""):
    """Return number of lines in text file"""
    with open(filename, mode="r", encoding="utf-8") as f:
        lines = 0
        for line in f:
            lines += 1
    return lines
