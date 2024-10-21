#!/usr/bin/python3
'''Module for testing the Rectangle class.'''
import unittest  # Importing the unittest module for testing
from models.base import Base  # Importing Base class from models
from models.rectangle import Rectangle  # Importing Rectangle class
from random import randrange  # Importing random number generator
from contextlib import redirect_stdout  # Redirect stdout for test purposes
import io  # Used to handle in-memory streams

class TestRectangle(unittest.TestCase):
    '''Test suite for Rectangle class behavior.'''

    def setUp(self):
        '''Reset class attributes before each test.'''
        Base._Base__nb_objects = 0  # Resetting the object counter

    def tearDown(self):
        '''Executed after each test method.'''
        pass  # No cleanup needed here

    # ----------------- Tests related to #2 ------------------------

    def test_A_class(self):
        '''Check if the class is correctly defined.'''
        self.assertEqual(str(Rectangle),
                         "<class 'models.rectangle.Rectangle'>")

    def test_B_inheritance(self):
        '''Verify Rectangle inherits from Base.'''
        self.assertTrue(issubclass(Rectangle, Base))

    def test_C_constructor_no_args(self):
        '''Ensure constructor raises TypeError with missing arguments.'''
        with self.assertRaises(TypeError) as e:
            r = Rectangle()  # No arguments given
        s = "__init__() missing 2 required positional arguments: 'width' and 'height'"
        self.assertEqual(str(e.exception), s)

    def test_C_constructor_many_args(self):
        '''Ensure constructor raises TypeError with extra arguments.'''
        with self.assertRaises(TypeError) as e:
            r = Rectangle(1, 2, 3, 4, 5, 6)  # Too many arguments
        s = "__init__() takes from 3 to 6 positional arguments but 7 were given"
        self.assertEqual(str(e.exception), s)

    def test_C_constructor_one_args(self):
        '''Ensure constructor raises TypeError when one argument is missing.'''
        with self.assertRaises(TypeError) as e:
            r = Rectangle(1)  # Only one argument given
        s = "__init__() missing 1 required positional argument: 'height'"
        self.assertEqual(str(e.exception), s)

    def test_D_instantiation(self):
        '''Test correct instantiation of a Rectangle object.'''
        r = Rectangle(10, 20)  # Creating a valid Rectangle
        self.assertEqual(str(type(r)), "<class 'models.rectangle.Rectangle'>")
        self.assertTrue(isinstance(r, Base))  # Check inheritance

        d = {'_Rectangle__height': 20, '_Rectangle__width': 10,
             '_Rectangle__x': 0, '_Rectangle__y': 0, 'id': 1}
        self.assertDictEqual(r.__dict__, d)  # Check internal attributes

        # Ensure invalid input types raise TypeError
        with self.assertRaises(TypeError) as e:
            r = Rectangle("1", 2)
        msg = "width must be an integer"
        self.assertEqual(str(e.exception), msg)

        with self.assertRaises(TypeError) as e:
            r = Rectangle(1, "2")
        msg = "height must be an integer"
        self.assertEqual(str(e.exception), msg)

        with self.assertRaises(TypeError) as e:
            r = Rectangle(1, 2, "3")
        msg = "x must be an integer"
        self.assertEqual(str(e.exception), msg)

        with self.assertRaises(TypeError) as e:
            r = Rectangle(1, 2, 3, "4")
        msg = "y must be an integer"
        self.assertEqual(str(e.exception), msg)

        # Ensure negative or zero values raise ValueError
        with self.assertRaises(ValueError) as e:
            r = Rectangle(-1, 2)
        msg = "width must be > 0"
        self.assertEqual(str(e.exception), msg)

        with self.assertRaises(ValueError) as e:
            r = Rectangle(1, -2)
        msg = "height must be > 0"
        self.assertEqual(str(e.exception), msg)

        with self.assertRaises(ValueError) as e:
            r = Rectangle(0, 2)
        msg = "width must be > 0"
        self.assertEqual(str(e.exception), msg)

        with self.assertRaises(ValueError) as e:
            r = Rectangle(1, 0)
        msg = "height must be > 0"
        self.assertEqual(str(e.exception), msg)

        with self.assertRaises(ValueError) as e:
            r = Rectangle(1, 2, -3)
        msg = "x must be >= 0"
        self.assertEqual(str(e.exception), msg)

        with self.assertRaises(ValueError) as e:
            r = Rectangle(1, 2, 3, -4)
        msg = "y must be >= 0"
        self.assertEqual(str(e.exception), msg)

    def test_D_instantiation_positional(self):
        '''Verify instantiation with positional arguments.'''
        r = Rectangle(5, 10, 15, 20)
        d = {'_Rectangle__height': 10, '_Rectangle__width': 5,
             '_Rectangle__x': 15, '_Rectangle__y': 20, 'id': 1}
        self.assertEqual(r.__dict__, d)

        r = Rectangle(5, 10, 15, 20, 98)
        d = {'_Rectangle__height': 10, '_Rectangle__width': 5,
             '_Rectangle__x': 15, '_Rectangle__y': 20, 'id': 98}
        self.assertEqual(r.__dict__, d)

    def test_D_instantiation_keyword(self):
        '''Verify instantiation with keyword arguments.'''
        r = Rectangle(100, 200, id=421, y=99, x=101)
        d = {'_Rectangle__height': 200, '_Rectangle__width': 100,
             '_Rectangle__x': 101, '_Rectangle__y': 99, 'id': 421}
        self.assertEqual(r.__dict__, d)

    def test_E_id_inherited(self):
        '''Check if id is inherited properly from Base.'''
        Base._Base__nb_objects = 98  # Set object counter manually
        r = Rectangle(2, 4)
        self.assertEqual(r.id, 99)  # Check inherited ID

    def test_F_properties(self):
        '''Test property getters and setters.'''
        r = Rectangle(5, 9)  # Instantiate a Rectangle
        r.width = 100  # Modify properties
        r.height = 101
        r.x = 102
        r.y = 103

        d = {'_Rectangle__height': 101, '_Rectangle__width': 100,
             '_Rectangle__x': 102, '_Rectangle__y': 103, 'id': 1}
        self.assertEqual(r.__dict__, d)  # Verify internal attributes

        # Verify individual getters
        self.assertEqual(r.width, 100)
        self.assertEqual(r.height, 101)
        self.assertEqual(r.x, 102)
        self.assertEqual(r.y, 103)

    # ----------------- More test cases available ------------------------

    # Additional test cases would follow the same structure, covering various
    # scenarios, including validation, area computation, display methods, and 
    # ensuring correct exceptions are raised under appropriate conditions.

if __name__ == "__main__":
    unittest.main()  # Run the test suite when the script is executed

