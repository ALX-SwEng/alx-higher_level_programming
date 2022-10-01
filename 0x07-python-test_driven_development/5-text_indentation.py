#!/usr/bin/python3
"""
This module defines `text_indentation`

The function prints a text with 2 new lines after each of
these characters: ., ? and :
"""

def text_indentation(text):
    """Prints a text with 2 new lines after these characters: ., ? and :"""

    leng = len(text)
    i = 0
    while i < leng:
        print(text[i], end='')
        if text[i] in [':', '.', '?']:
            print('\n')
            if i + 1 == leng:
                break
            if i < leng and text[i + 1] == ' ':
                i += 1
        i += 1
