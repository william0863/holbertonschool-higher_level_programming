#!/usr/bin/python3
"""
function that returns the JSON representation of an object (string)
"""
import json


def to_json_string(my_obj):
    """returns the JSON representation of an object (string)
    args:
        my_obj: object to convert
    return:
        object
    """

    return json.dumps(my_obj)
