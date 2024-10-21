#!/usr/bin/python3
'''Module defining the Square class, derived from Rectangle.'''
from models.rectangle import Rectangle


class Square(Rectangle):
    '''Class representing a square shape.'''

    def __init__(self, size, x=0, y=0, id=None):
        '''Initialize a new Square instance.'''
        super().__init__(size, size, x, y, id)  # Call the Rectangle constructor

    def __str__(self):
        '''Return a string representation of the square.'''
        return '[{}] ({}) {}/{} - {}'.format(
            type(self).__name__, self.id, self.x, self.y, self.width)

    @property
    def size(self):
        '''Return the size (width) of the square.'''
        return self.width  # Size is the same as width

    @size.setter
    def size(self, value):
        '''Set the size of the square, updating both width and height.'''
        self.width = value  # Set width
        self.height = value  # Set height to maintain square properties

    def __update(self, id=None, size=None, x=None, y=None):
        '''Internal method to update attributes of the square.'''
        if id is not None:
            self.id = id  # Update id if provided
        if size is not None:
            self.size = size  # Update size (and width/height)
        if x is not None:
            self.x = x  # Update x-coordinate if provided
        if y is not None:
            self.y = y  # Update y-coordinate if provided

    def update(self, *args, **kwargs):
        '''Update square attributes using positional and/or keyword arguments.'''
        if args:
            self.__update(*args)  # Update using positional arguments
        elif kwargs:
            self.__update(**kwargs)  # Update using keyword arguments

    def to_dictionary(self):
        '''Return a dictionary representation of the square.'''
        return {
            "id": self.id,
            "size": self.width,  # Size is represented by width
            "x": self.x,
            "y": self.y
        }  # Construct and return dictionary representation
