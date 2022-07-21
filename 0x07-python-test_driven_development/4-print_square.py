#!/usr/bin/python3

"""Defines a print_square function."""

from logging import exception


def print_square(size):
    """Prints a square with the character #

    Args:
        size(int): the size length of the square.

    Raises:
        TypeError exception: If the size is not integer or a float less than zero.
        ValueError exception: If the size is less than zero.

    Returns:
        None.
"""
    if not isinstance(size, int) or (isinstance(size, float) and size < 0): 
        raise TypeError ("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    
    for row in range (size):
        [print("#", end="") for col in range(size)]
        print("")