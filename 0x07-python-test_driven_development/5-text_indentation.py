#!/usr/bin/python3
"""
This module defines `text_indentation`
The function prints a text with 2 new lines after each of
these characters: ., ? and :
"""


def text_indentation(text):
    """splits a text into lines along "?", ":", "." followed by 2 new lines
    Args:
        text: input string
    Returns:
        No return
    Raises:
        TypeError: If text is not a string
    """

    if type(text) is not str:
        raise TypeError("text must be a string")
    flag = 0
    a = 0
    for a < len(text):
        if flag == 0:
            if text[a] == ' ':
                continue
            else:
                flag = 1
        if flag == 1:
            if text[a] == '?' or text[a] == '.' or text[a] == ':':
                print(text[a])
                print()
                flag = 0
            else:
                print(text[a], end="")
