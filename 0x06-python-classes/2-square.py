#!/usr/bin/python3
"""Defines a class Square."""


class Square:
    """Represents a square."""
    
   
    def __int__(self, size):
        """Initializes a new Square.

        Args:
            size (int): The size of the new square.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
        