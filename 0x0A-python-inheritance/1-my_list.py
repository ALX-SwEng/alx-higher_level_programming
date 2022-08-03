#!/usr/bin/python3
"""
contains the MyList class
"""


class MyList(list):
    """a subclass of list"""
    def __init__(self, lists=None):
        """initializes the object"""
        super().__init__(lists)

    def print_sorted(self):
        """prints the sorted list"""
        print(sorted(self))
