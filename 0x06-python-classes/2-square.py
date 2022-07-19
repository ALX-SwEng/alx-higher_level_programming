#!/usr/bin/python3
"""Defines a class Square."""


class Square:
    """Represents a square."""
    
   
    def __int__(self, size):
        """Initializes a new Square.

        Args:
            size (int): The size of the new square.
        """
        try:
            self.__size = size
        except TypeError:
            print("size must be an integer")
        except ValueError:
            print("size must be >= 0")