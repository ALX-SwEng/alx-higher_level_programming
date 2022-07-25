#!/usr/bin/python3
"""Defines a class Rectangle"""


class Rectangle:
    """Represents a rectangle. No body."""

    def __init__(self, width=0, height=0):
        """Initialize a new Rectangle.

        Args:
            width (int): The width of the new rectangle.
            height (int): The height of the new rectangle.
        """
        self.width = width
        self.height = height
    
    @property
    def width(self):
        """ return width of rectangle """
        return self.__width

    @width.setter
    def width(self, value):
        """ set width of rectangle 
                
        Args:
            value (int): must be a +ve integer
        
        Raises:
            TypeError exception: If value is not an integer.
            ValueError exception: if value is less than zero
        """
        
        if not isinstance (value, int):
            raise TypeError("Width must be an integer")
        if value < 0:
            raise ValueError("Width must be >= 0")

        self.__width = value
    
    @property
    def height(self):
        """ return height of rectangle """
        return self.__height

    @height.setter
    def height(self, value):
        """ set height of rectangle 
        
        Args:
            value (int): must be a +ve integer
        
        Raises:
            TypeError exception: If value is not an integer.
            ValueError exception: if value is less than zero
        """

        if not isinstance (value, int):
            raise TypeError("Height must be an integer")
        if value < 0:
            raise ValueError("Height must be >= 0")

        self.__height = value

    def area(self): 
        """ that returns the rectangle area """
        return self.__width * self.__height

    def perimeter(self): 
        """that returns the rectangle perimeter"""
        if self.__width == 0 or self.__height == 0:
            return (0)
            
        return 2 * (self.__width + self.__height)

    def __str__(self):
        """Return the printable representation of the Rectangle.

        Represents the rectangle with the # character.
        """
        if self.__width == 0 or self.__height == 0:
            return ("")

        rect = []
        for i in range(self.__height):
            [rect.append('#') for j in range(self.__width)]
            if i != self._height - 1:
                rect.append('\n')
        return ("".join(rect))