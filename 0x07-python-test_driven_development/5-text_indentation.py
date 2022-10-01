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
    leng = 0
    while leng  < len(text):
        if flag == 0:
            if text[leng] == ' ':
                continue
            else:
                flag = 1
        if flag == 1:
            if text[leng] == '?' or text[leng] == '.' or text[leng] == ':':
                print(a)
                print()
                flag = 0
            else:
                if text[leng] == " " and text[leng+1] == '\n':
                    continue;
                print(a, end="")
                if a == '\n':
                    flag = 0
