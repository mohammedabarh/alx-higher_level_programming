#!/usr/bin/python3
'''Module defining the Square class.'''
from models.rectangle import Rectangle


class Square(Rectangle):
    '''Class representing a square, inheriting from Rectangle.'''

    def __init__(self, size, x=0, y=0, id=None):
        '''Initialize a new Square instance.'''
        super().__init__(size, size, x, y, id)  # Call the constructor of the Rectangle class

    def __str__(self):
        '''Return a string representation of the square for display.'''
        return '[{}] ({}) {}/{} - {}'.format(
            type(self).__name__, self.id, self.x, self.y, self.width)  # Format output string

    @property
    def size(self):
        '''Get the size of the square.'''
        return self.width  # Size is equivalent to the width

    @size.setter
    def size(self, value):
        '''Set the size of the square, updating both width and height.'''
        self.width = value  # Update width
        self.height = value  # Update height

    def __update(self, id=None, size=None, x=None, y=None):
        '''Internal method to update attributes using provided arguments.'''
        if id is not None:
            self.id = id  # Update ID if provided
        if size is not None:
            self.size = size  # Update size if provided
        if x is not None:
            self.x = x  # Update x-coordinate if provided
        if y is not None:
            self.y = y  # Update y-coordinate if provided

    def update(self, *args, **kwargs):
        '''Update instance attributes using positional or keyword arguments.'''
        if args:
            self.__update(*args)  # Update using positional arguments
        elif kwargs:
            self.__update(**kwargs)  # Update using keyword arguments

    def to_dictionary(self):
        '''Return a dictionary representation of the square.'''
        return {
            "id": self.id,
            "size": self.width,  # Size matches the width
            "x": self.x,
            "y": self.y
        }  # Create and return dictionary representation
