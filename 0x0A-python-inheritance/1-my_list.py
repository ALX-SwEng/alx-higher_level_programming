#!/usr/bin/python3
"""
Defines MyList that inherits from list
"""


class MyList(list):
    """
        This class inherits from list.
        Attributes:
        Methods:
            print_sorted - prints the list in ascending order
    """
    def print_sorted(self):
        """
           prints a list in ascending order.
        """
        print(sorted(self))
        
