#!/usr/bin/python3

"""Defines a print_square function."""

def text_indentation(text):
    """Prints a text with 2 new lines after each of these characters: ., ? and :

    Args:
        text(str): the string to print.

    Raises:
        TypeError exception: If the text is not string.
    """
    if not isinstance(text, str): 
        raise TypeError ("text must be an string")
    i = 0
    while i < len(text) and text[i] == ' ':
        i += 1

    while i < len(text):
        print(text[i], end="")
        if text[i] in ".?:":
            print("\n")
        while i < len(text) and text[i] == ' ':
            i += 1
        i +=1
        