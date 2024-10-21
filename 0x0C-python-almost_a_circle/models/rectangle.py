#!/usr/bin/python3
'''Module defining the Rectangle class, derived from Base.'''
from models.base import Base


class Rectangle(Base):
    '''Class representing a rectangle shape.'''

    def __init__(self, width, height, x=0, y=0, id=None):
        '''Initialize a new Rectangle instance.'''
        super().__init__(id)  # Call the constructor of the Base class
        self.width = width    # Set the width of the rectangle
        self.height = height  # Set the height of the rectangle
        self.x = x           # Set the x-coordinate of the rectangle
        self.y = y           # Set the y-coordinate of the rectangle

    @property
    def width(self):
        '''Return the width of the rectangle.'''
        return self.__width

    @width.setter
    def width(self, value):
        '''Set the width of the rectangle after validation.'''
        self.validate_integer("width", value, False)  # Validate width
        self.__width = value  # Assign value to width

    @property
    def height(self):
        '''Return the height of the rectangle.'''
        return self.__height

    @height.setter
    def height(self, value):
        '''Set the height of the rectangle after validation.'''
        self.validate_integer("height", value, False)  # Validate height
        self.__height = value  # Assign value to height

    @property
    def x(self):
        '''Return the x-coordinate of the rectangle.'''
        return self.__x

    @x.setter
    def x(self, value):
        '''Set the x-coordinate of the rectangle after validation.'''
        self.validate_integer("x", value)  # Validate x
        self.__x = value  # Assign value to x

    @property
    def y(self):
        '''Return the y-coordinate of the rectangle.'''
        return self.__y

    @y.setter
    def y(self, value):
        '''Set the y-coordinate of the rectangle after validation.'''
        self.validate_integer("y", value)  # Validate y
        self.__y = value  # Assign value to y

    def validate_integer(self, name, value, eq=True):
        '''Validate that value is an integer and meets specified conditions.'''
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))  # Type check
        if eq and value < 0:
            raise ValueError("{} must be >= 0".format(name))  # Minimum value check
        elif not eq and value <= 0:
            raise ValueError("{} must be > 0".format(name))  # Positive value check

    def area(self):
        '''Calculate the area of the rectangle.'''
        return self.width * self.height  # Area calculation

    def display(self):
        '''Print the rectangle using the '#' character.'''
        s = '\n' * self.y + \
            (' ' * self.x + '#' * self.width + '\n') * self.height
        print(s, end='')  # Output rectangle representation

    def __str__(self):
        '''Return a string representation of the rectangle.'''
        return '[{}] ({}) {}/{} - {}/{}'.format(
            type(self).__name__, self.id, self.x, self.y, self.width, self.height)

    def __update(self, id=None, width=None, height=None, x=None, y=None):
        '''Internal method to update attributes of the rectangle.'''
        if id is not None:
            self.id = id  # Update id if provided
        if width is not None:
            self.width = width  # Update width if provided
        if height is not None:
            self.height = height  # Update height if provided
        if x is not None:
            self.x = x  # Update x if provided
        if y is not None:
            self.y = y  # Update y if provided

    def update(self, *args, **kwargs):
        '''Update rectangle attributes using positional and/or keyword arguments.'''
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
        }  # Construct and return dictionary representation#!/usr/bin/python3
'''Module defining the Rectangle class, derived from Base.'''
from models.base import Base


class Rectangle(Base):
    '''Class representing a rectangle shape.'''

    def __init__(self, width, height, x=0, y=0, id=None):
        '''Initialize a new Rectangle instance.'''
        super().__init__(id)  # Call the constructor of the Base class
        self.width = width    # Set the width of the rectangle
        self.height = height  # Set the height of the rectangle
        self.x = x           # Set the x-coordinate of the rectangle
        self.y = y           # Set the y-coordinate of the rectangle

    @property
    def width(self):
        '''Return the width of the rectangle.'''
        return self.__width

    @width.setter
    def width(self, value):
        '''Set the width of the rectangle after validation.'''
        self.validate_integer("width", value, False)  # Validate width
        self.__width = value  # Assign value to width

    @property
    def height(self):
        '''Return the height of the rectangle.'''
        return self.__height

    @height.setter
    def height(self, value):
        '''Set the height of the rectangle after validation.'''
        self.validate_integer("height", value, False)  # Validate height
        self.__height = value  # Assign value to height

    @property
    def x(self):
        '''Return the x-coordinate of the rectangle.'''
        return self.__x

    @x.setter
    def x(self, value):
        '''Set the x-coordinate of the rectangle after validation.'''
        self.validate_integer("x", value)  # Validate x
        self.__x = value  # Assign value to x

    @property
    def y(self):
        '''Return the y-coordinate of the rectangle.'''
        return self.__y

    @y.setter
    def y(self, value):
        '''Set the y-coordinate of the rectangle after validation.'''
        self.validate_integer("y", value)  # Validate y
        self.__y = value  # Assign value to y

    def validate_integer(self, name, value, eq=True):
        '''Validate that value is an integer and meets specified conditions.'''
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))  # Type check
        if eq and value < 0:
            raise ValueError("{} must be >= 0".format(name))  # Minimum value check
        elif not eq and value <= 0:
            raise ValueError("{} must be > 0".format(name))  # Positive value check

    def area(self):
        '''Calculate the area of the rectangle.'''
        return self.width * self.height  # Area calculation

    def display(self):
        '''Print the rectangle using the '#' character.'''
        s = '\n' * self.y + \
            (' ' * self.x + '#' * self.width + '\n') * self.height
        print(s, end='')  # Output rectangle representation

    def __str__(self):
        '''Return a string representation of the rectangle.'''
        return '[{}] ({}) {}/{} - {}/{}'.format(
            type(self).__name__, self.id, self.x, self.y, self.width, self.height)

    def __update(self, id=None, width=None, height=None, x=None, y=None):
        '''Internal method to update attributes of the rectangle.'''
        if id is not None:
            self.id = id  # Update id if provided
        if width is not None:
            self.width = width  # Update width if provided
        if height is not None:
            self.height = height  # Update height if provided
        if x is not None:
            self.x = x  # Update x if provided
        if y is not None:
            self.y = y  # Update y if provided

    def update(self, *args, **kwargs):
        '''Update rectangle attributes using positional and/or keyword arguments.'''
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
        }  # Construct and return dictionary representation
