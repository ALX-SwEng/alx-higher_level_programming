#!/usr/bin/python3
"""
This module defines `text_indentation`

The function prints a text with 2 new lines after each of
these characters: ., ? and :
"""


def text_indentation(text):
    """splits a text into lines along "?", ":", "." followed by 2 new lines"""
    if type(text) is not str:
        raise TypeError("text must be a string")

    endings = [".", "?", ":"]
    for i in text:
        if i in endings:
            print(f"{i}\n")
        else:
            print(i, end="")
