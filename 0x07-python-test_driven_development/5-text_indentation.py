#!/usr/bin/python3
"""
This module defines `text_indentation`
The function prints a text with 2 new lines after each of
these characters: ., ? and :
"""


def text_indentation(text):
    """Prit a text with 2 new lines after each characters"""

    if type(text) != str:
        raise TypeError("text must be a string")
    flag = 0
    i = 0
    while i < len(text):
        if flag == 0:
            if text[i] == ' ':
                continue
            else:
                flag = 1
        if flag == 1:
            if text[i] == '?' or text[i] == '.' or text[i] == ':':
                print(text[i])
                print()
                flag = 0
            else:
                print(text[i], end="")
