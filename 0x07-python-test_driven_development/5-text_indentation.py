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
    for a in text:
        if flag == 0:
            if a == ' ':
                continue
            else:
                flag = 1
        if flag == 1:
            if a == '?' or a == '.' or a == ':':
                print(a)
                print()
                flag = 0
            else:
                print(a, end="")
                if a == '\n':
                    flag = 0
