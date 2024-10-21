#!/usr/bin/python3
'''Module defining the Base class for the OOP hierarchy.'''
from json import dumps, loads
import csv


class Base:
    '''Base class representing the foundation of our object-oriented design.'''

    __nb_objects = 0  # Class variable to track the number of instances

    def __init__(self, id=None):
        '''Initialize a new Base instance.'''
        if id is not None:
            self.id = id  # Set the id if provided
        else:
            Base.__nb_objects += 1  # Increment the number of objects
            self.id = Base.__nb_objects  # Assign an id

    @staticmethod
    def to_json_string(list_dictionaries):
        '''Convert a list of dictionaries to a JSON string.'''
        if list_dictionaries is None or not list_dictionaries:
            return "[]"  # Return empty JSON array if input is empty
        else:
            return dumps(list_dictionaries)  # Serialize the list to JSON

    @staticmethod
    def from_json_string(json_string):
        '''Convert a JSON string back to a list of dictionaries.'''
        if json_string is None or not json_string:
            return []  # Return an empty list for empty input
        return loads(json_string)  # Deserialize the JSON string

    @classmethod
    def save_to_file(cls, list_objs):
        '''Save JSON representation of objects to a file.'''
        if list_objs is not None:
            list_objs = [o.to_dictionary() for o in list_objs]  # Convert objects to dictionaries
        with open("{}.json".format(cls.__name__), "w", encoding="utf-8") as f:
            f.write(cls.to_json_string(list_objs))  # Write JSON string to file

    @classmethod
    def load_from_file(cls):
        '''Load objects from a JSON file.'''
        from os import path
        file = "{}.json".format(cls.__name__)
        if not path.isfile(file):
            return []  # Return an empty list if the file does not exist
        with open(file, "r", encoding="utf-8") as f:
            return [cls.create(**d) for d in cls.from_json_string(f.read())]  # Create instances from file data

    @classmethod
    def create(cls, **dictionary):
        '''Create an instance of the class from a dictionary.'''
        from models.rectangle import Rectangle
        from models.square import Square
        if cls is Rectangle:
            new = Rectangle(1, 1)  # Default values for Rectangle
        elif cls is Square:
            new = Square(1)  # Default values for Square
        else:
            new = None  # Handle other cases
        new.update(**dictionary)  # Update instance attributes from the dictionary
        return new

    @classmethod
    def save_to_file_csv(cls, list_objs):
        '''Save object data to a CSV file.'''
        from models.rectangle import Rectangle
        from models.square import Square
        if list_objs is not None:
            if cls is Rectangle:
                list_objs = [[o.id, o.width, o.height, o.x, o.y] for o in list_objs]  # Prepare data for Rectangle
            else:
                list_objs = [[o.id, o.size, o.x, o.y] for o in list_objs]  # Prepare data for Square
        with open('{}.csv'.format(cls.__name__), 'w', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerows(list_objs)  # Write data rows to the CSV file

    @classmethod
    def load_from_file_csv(cls):
        '''Load object data from a CSV file.'''
        from models.rectangle import Rectangle
        from models.square import Square
        ret = []  # List to hold created instances
        with open('{}.csv'.format(cls.__name__), 'r', newline='', encoding='utf-8') as f:
            reader = csv.reader(f)
            for row in reader:
                row = [int(r) for r in row]  # Convert strings to integers
                if cls is Rectangle:
                    d = {"id": row[0], "width": row[1], "height": row[2], "x": row[3], "y": row[4]}
                else:
                    d = {"id": row[0], "size": row[1], "x": row[2], "y": row[3]}
                ret.append(cls.create(**d))  # Create instances from the dictionary
        return ret  # Return the list of instances

    @staticmethod
    def draw(list_rectangles, list_squares):
        '''Draw rectangles and squares using the turtle graphics module.'''
        import turtle
        import time
        from random import randrange
        turtle.Screen().colormode(255)  # Set color mode for turtle
        for i in list_rectangles + list_squares:
            t = turtle.Turtle()  # Create a new turtle for drawing
            t.color((randrange(255), randrange(255), randrange(255)))  # Set a random color
            t.pensize(1)  # Set pen size
            t.penup()
            t.pendown()
            t.setpos((i.x + t.pos()[0], i.y - t.pos()[1]))  # Move turtle to starting position
            t.pensize(10)
            t.forward(i.width)  # Draw the width
            t.left(90)
            t.forward(i.height)  # Draw the height
            t.left(90)
            t.forward(i.width)  # Complete the rectangle
            t.left(90)
            t.forward(i.height)
            t.left(90)
            t.end_fill()  # Fill the shape

        time.sleep(5)
