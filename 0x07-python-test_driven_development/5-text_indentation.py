#!/usr/bin/python3
"""
This module defines `text_indentation`

The function prints a text with 2 new lines after each of
these characters: ., ? and :
"""


def text_indentation(text):
    """ Function that prints 2 new lines after ".?:" characters
    Args:
        text: input string
    Returns:
        No return
    Raises:
        TypeError: If text is not a string
    """

    if type(text) is not str:
        raise TypeError("text must be a string")

    s = text[:]

    for chars in ".?:":
        list_text = s.split(chars)
        s = ""
        for i in list_text:
            i = i.strip(" ")
            s = i + chars if s == "" else s + "\n\n" + i + chars

    print(s[:-3], end="")
