#!/usr/bin/python3
'''Module defining the Rectangle class.'''
from models.base import Base


class Rectangle(Base):
    '''Class representing a rectangle.'''

    def __init__(self, width, height, x=0, y=0, id=None):
        '''Initialize a new Rectangle instance.'''
        super().__init__(id)  # Call the constructor of the Base class
        self.width = width  # Set width of the rectangle
        self.height = height  # Set height of the rectangle
        self.x = x  # Set x-coordinate of the rectangle
        self.y = y  # Set y-coordinate of the rectangle

    @property
    def width(self):
        '''Get the width of the rectangle.'''
        return self.__width

    @width.setter
    def width(self, value):
        '''Set the width of the rectangle with validation.'''
        self.validate_integer("width", value, False)  # Validate width
        self.__width = value  # Assign width

    @property
    def height(self):
        '''Get the height of the rectangle.'''
        return self.__height

    @height.setter
    def height(self, value):
        '''Set the height of the rectangle with validation.'''
        self.validate_integer("height", value, False)  # Validate height
        self.__height = value  # Assign height

    @property
    def x(self):
        '''Get the x-coordinate of the rectangle.'''
        return self.__x

    @x.setter
    def x(self, value):
        '''Set the x-coordinate of the rectangle with validation.'''
        self.validate_integer("x", value)  # Validate x-coordinate
        self.__x = value  # Assign x-coordinate

    @property
    def y(self):
        '''Get the y-coordinate of the rectangle.'''
        return self.__y

    @y.setter
    def y(self, value):
        '''Set the y-coordinate of the rectangle with validation.'''
        self.validate_integer("y", value)  # Validate y-coordinate
        self.__y = value  # Assign y-coordinate

    def validate_integer(self, name, value, eq=True):
        '''Validate that a value is an integer with constraints.'''
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))  # Raise error for non-integer
        if eq and value < 0:
            raise ValueError("{} must be >= 0".format(name))  # Raise error for negative value
        elif not eq and value <= 0:
            raise ValueError("{} must be > 0".format(name))  # Raise error for non-positive value

    def area(self):
        '''Calculate and return the area of the rectangle.'''
        return self.width * self.height  # Area calculation

    def display(self):
        '''Print the visual representation of the rectangle.'''
        s = '\n' * self.y + \
            (' ' * self.x + '#' * self.width + '\n') * self.height  # Build the string representation
        print(s, end='')  # Print the rectangle to the console

    def __str__(self):
        '''Return a string representation of the rectangle for display.'''
        return '[{}] ({}) {}/{} - {}/{}'.format(
            type(self).__name__, self.id, self.x, self.y, self.width, self.height)  # Format string output

    def __update(self, id=None, width=None, height=None, x=None, y=None):
        '''Internal method to update attributes using provided arguments.'''
        if id is not None:
            self.id = id  # Update ID if provided
        if width is not None:
            self.width = width  # Update width if provided
        if height is not None:
            self.height = height  # Update height if provided
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
        '''Return a dictionary representation of the rectangle.'''
        return {
            "id": self.id,
            "width": self.__width,
            "height": self.__height,
            "x": self.__x,
            "y": self.__y
        }  # Create and return dictionary representation
