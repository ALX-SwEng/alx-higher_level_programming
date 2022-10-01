#!/usr/bin/python3
"""
This module defines `text_indentation`

The function prints a text with 2 new lines after each of
these characters: ., ? and :
"""


def text_indentation(text):
    """adds paragraph after `.`, `:` and `?`

    Args:
        text (str)
    """
    if not isinstance(text, str):
        raise TypeError('text must be a string')

    for l in '.:?':
        text = text.replace(l, '{}\n'.format(l))
    lines = text.splitlines()
    for index, line in enumerate(lines):
        print(line.strip(), end='' if index == len(lines) - 1 else '\n\n')
