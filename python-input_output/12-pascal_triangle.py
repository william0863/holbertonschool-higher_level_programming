#!/usr/bin/python3
"""
function def pascal_triangle(n): that returns a list of lists of integers
representing the Pascal’s triangle of n
"""


def pascal_triangle(n):
    """calculate pascal
    args:
        n: value
    return
        list
    """
    my_list = []
    if n <= 0:
        return my_list
    for i in range(n):
        num = 11**i
        li = [int(n) for n in str(num)]
        my_list.append(li)
    return my_list
