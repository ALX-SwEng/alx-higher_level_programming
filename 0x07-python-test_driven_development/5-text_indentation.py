#!/usr/bin/python3

"""Defines a print_square function."""

def text_indentation(text):
    """Prints a text with 2 new lines after each of these characters: ., ? and :

    Args:
        text(str): the string to print.

    Raises:
        TypeError exception: If the text is not string.

    Returns:
        None.
"""
    if not isinstance(text, str): 
        raise TypeError ("text must be an string")
    
    for character in range (text):
        print(character)
        if character in [".?:"]:
            print("\n")
        