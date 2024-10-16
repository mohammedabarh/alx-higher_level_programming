#!/usr/bin/python3
"""Module for student creation and management."""


class Student:
    """Represents a student with a first name, last name, and age."""
    
    def __init__(self, first_name, last_name, age):
        """Initialize a new student instance."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Return a dictionary representation of the Student instance.
        
        If attrs is provided, only the attributes specified in attrs
        will be included in the returned dictionary.
        """
        if attrs is None:
            return self.__dict__
        new_dictionary = {}
        for key, value in self.__dict__.items():
            if key in attrs:
                new_dictionary[key] = value
        return new_dictionary

    def reload_from_json(self, json):
        """Update the Student instance with values from a JSON dictionary."""
        for key, value in json.items():
            setattr(self, key, value)
