#!/usr/bin/python3
'''Base class module for object-oriented programming hierarchy.'''
from json import dumps, loads
import csv


class Base:
    '''Base class representing the foundation of our OOP hierarchy.'''

    __nb_objects = 0  # Class variable to keep track of object instances

    def __init__(self, id=None):
        '''Initialize a new Base instance with a unique ID.'''
        if id is not None:
            self.id = id  # Assign provided ID
        else:
            Base.__nb_objects += 1  # Increment object count
            self.id = Base.__nb_objects  # Assign new unique ID

    @staticmethod
    def to_json_string(list_dictionaries):
        '''Convert a list of dictionaries to a JSON string.'''
        if list_dictionaries is None or not list_dictionaries:
            return "[]"  # Return empty JSON array for None or empty list
        return dumps(list_dictionaries)  # Return JSON string representation

    @staticmethod
    def from_json_string(json_string):
        '''Convert a JSON string back to a list of dictionaries.'''
        if json_string is None or not json_string:
            return []  # Return empty list for None or empty string
        return loads(json_string)  # Return list representation from JSON

    @classmethod
    def save_to_file(cls, list_objs):
        '''Save a list of objects as a JSON string to a file.'''
        if list_objs is not None:
            list_objs = [o.to_dictionary() for o in list_objs]  # Convert objects to dictionaries
        with open("{}.json".format(cls.__name__), "w", encoding="utf-8") as f:
            f.write(cls.to_json_string(list_objs))  # Write JSON string to file

    @classmethod
    def create(cls, **dictionary):
        '''Create an instance from a dictionary of attributes.'''
        from models.rectangle import Rectangle
        from models.square import Square
        if cls is Rectangle:
            new = Rectangle(1, 1)  # Create a default Rectangle object
        elif cls is Square:
            new = Square(1)  # Create a default Square object
        else:
            new = None  # Unsupported class
        new.update(**dictionary)  # Update the object's attributes
        return new  # Return the newly created instance

    @classmethod
    def load_from_file(cls):
        '''Load objects from a JSON file and return a list of instances.'''
        from os import path
        file = "{}.json".format(cls.__name__)
        if not path.isfile(file):
            return []  # Return empty list if file does not exist
        with open(file, "r", encoding="utf-8") as f:
            return [cls.create(**d) for d in cls.from_json_string(f.read())]  # Create instances from JSON data

    @classmethod
    def save_to_file_csv(cls, list_objs):
        '''Save a list of objects to a CSV file.'''
        from models.rectangle import Rectangle
        from models.square import Square
        if list_objs is not None:
            if cls is Rectangle:
                list_objs = [[o.id, o.width, o.height, o.x, o.y] for o in list_objs]  # Extract Rectangle attributes
            else:
                list_objs = [[o.id, o.size, o.x, o.y] for o in list_objs]  # Extract Square attributes
        with open('{}.csv'.format(cls.__name__), 'w', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerows(list_objs)  # Write object data to CSV

    @classmethod
    def load_from_file_csv(cls):
        '''Load objects from a CSV file and return a list of instances.'''
        from models.rectangle import Rectangle
        from models.square import Square
        ret = []
        with open('{}.csv'.format(cls.__name__), 'r', newline='', encoding='utf-8') as f:
            reader = csv.reader(f)
            for row in reader:
                row = [int(r) for r in row]  # Convert string data to integers
                if cls is Rectangle:
                    d = {"id": row[0], "width": row[1], "height": row[2], "x": row[3], "y": row[4]}  # Dictionary for Rectangle
                else:
                    d = {"id": row[0], "size": row[1], "x": row[2], "y": row[3]}  # Dictionary for Square
                ret.append(cls.create(**d))  # Create instance and append to list
        return ret  # Return list of instances

    @staticmethod
    def draw(list_rectangles, list_squares):
        '''Draw rectangles and squares using turtle graphics.'''
        import turtle
        import time
        from random import randrange
        turtle.Screen().colormode(255)  # Set color mode to RGB
        for i in list_rectangles + list_squares:
            t = turtle.Turtle()
            t.color((randrange(255), randrange(255), randrange(255)))  # Random color for each shape
            t.pensize(1)
            t.penup()
            t.pendown()
            t.setpos((i.x + t.pos()[0], i.y - t.pos()[1]))  # Position turtle
            t.pensize(10)
            t.forward(i.width)  # Draw shape
            t.left(90)
            t.forward(i.height)
            t.left(90)
            t.forward(i.width)
            t.left(90)
            t.forward(i.height)
            t.left(90)
            t.end_fill()  # Fill the shape with color

        time.sleep(5)  # Pause to display the drawing
