#!/usr/bin/python3
"""Defines a name-printing function."""


def say_my_name(first_name, last_name=""):
    """Print full name as My name is <first name> <last name>.

    Args:
        first_name: a sirng, the first name to print.
        last_name: a string, the last name to print.
    Raises:
        TypeError: If first name and last name is not string.
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
