#!/usr/bin/python3
'''Unit tests for the Square class.'''
import unittest  # Importing the unittest module for test case management
from models.base import Base  # Import Base class from the models package
from models.square import Square  # Import Square class for testing
from random import randrange  # Importing random number generator for testing
from contextlib import redirect_stdout  # Redirect stdout for capturing outputs
import io  # In-memory I/O handling for testing printed outputs

class TestSquare(unittest.TestCase):
    '''Test suite for the Square class.'''

    def setUp(self):
        '''Resets the state before every test method.'''
        Base._Base__nb_objects = 0  # Reset the Base class counter

    def tearDown(self):
        '''Cleanup executed after each test method.'''
        pass  # No specific cleanup actions required here

    # ----------------- Class and Constructor Tests ------------------------

    def test_A_class(self):
        '''Checks if the class is properly defined.'''
        self.assertEqual(str(Square), "<class 'models.square.Square'>")

    def test_B_inheritance(self):
        '''Validates that Square inherits from Base.'''
        self.assertTrue(issubclass(Square, Base))

    def test_C_constructor_no_args(self):
        '''Tests constructor with no arguments.'''
        with self.assertRaises(TypeError) as e:
            r = Square()  # Constructor without required arguments
        expected_msg = "__init__() missing 1 required positional argument: 'size'"
        self.assertEqual(str(e.exception), expected_msg)

    def test_C_constructor_many_args(self):
        '''Tests constructor with too many arguments.'''
        with self.assertRaises(TypeError) as e:
            r = Square(1, 2, 3, 4, 5)  # Too many arguments passed
        expected_msg = "__init__() takes from 2 to 5 positional arguments but 6 were given"
        self.assertEqual(str(e.exception), expected_msg)

    def test_D_instantiation(self):
        '''Validates proper instantiation of Square.'''
        r = Square(10)  # Create a valid Square instance
        self.assertEqual(str(type(r)), "<class 'models.square.Square'>")
        self.assertTrue(isinstance(r, Base))  # Verify inheritance from Base

        # Check internal attributes
        expected_dict = {'_Rectangle__height': 10, '_Rectangle__width': 10,
                         '_Rectangle__x': 0, '_Rectangle__y': 0, 'id': 1}
        self.assertDictEqual(r.__dict__, expected_dict)

        # Check for TypeError on invalid input types
        with self.assertRaises(TypeError) as e:
            r = Square("1")  # Invalid size type
        self.assertEqual(str(e.exception), "width must be an integer")

        with self.assertRaises(TypeError) as e:
            r = Square(1, "2")  # Invalid x type
        self.assertEqual(str(e.exception), "x must be an integer")

        with self.assertRaises(TypeError) as e:
            r = Square(1, 2, "3")  # Invalid y type
        self.assertEqual(str(e.exception), "y must be an integer")

        # Check for ValueError on invalid size and position values
        with self.assertRaises(ValueError) as e:
            r = Square(-1)  # Negative size
        self.assertEqual(str(e.exception), "width must be > 0")

        with self.assertRaises(ValueError) as e:
            r = Square(1, -2)  # Negative x value
        self.assertEqual(str(e.exception), "x must be >= 0")

        with self.assertRaises(ValueError) as e:
            r = Square(1, 2, -3)  # Negative y value
        self.assertEqual(str(e.exception), "y must be >= 0")

        with self.assertRaises(ValueError) as e:
            r = Square(0)  # Size cannot be zero
        self.assertEqual(str(e.exception), "width must be > 0")

    def test_D_instantiation_positional(self):
        '''Checks instantiation with positional arguments.'''
        r = Square(5, 10, 15)  # Valid positional arguments
        expected_dict = {'_Rectangle__height': 5, '_Rectangle__width': 5,
                         '_Rectangle__x': 10, '_Rectangle__y': 15, 'id': 1}
        self.assertEqual(r.__dict__, expected_dict)

        r = Square(5, 10, 15, 20)  # Custom ID provided
        expected_dict['id'] = 20
        self.assertEqual(r.__dict__, expected_dict)

    def test_D_instantiation_keyword(self):
        '''Checks instantiation with keyword arguments.'''
        r = Square(100, id=421, y=99, x=101)
        expected_dict = {'_Rectangle__height': 100, '_Rectangle__width': 100,
                         '_Rectangle__x': 101, '_Rectangle__y': 99, 'id': 421}
        self.assertEqual(r.__dict__, expected_dict)

    def test_E_id_inherited(self):
        '''Verifies that ID is inherited from Base.'''
        Base._Base__nb_objects = 98  # Reset the counter manually
        r = Square(2)  # Create a Square instance
        self.assertEqual(r.id, 99)  # Check if the ID increments correctly

    def test_F_properties(self):
        '''Tests property setters and getters.'''
        r = Square(5, 9)  # Create a Square instance
        r.size = 98  # Set new size
        r.x = 102  # Set new x value
        r.y = 103  # Set new y value

        # Verify internal attributes
        expected_dict = {'_Rectangle__height': 98, '_Rectangle__width': 98,
                         '_Rectangle__x': 102, '_Rectangle__y': 103, 'id': 1}
        self.assertEqual(r.__dict__, expected_dict)

        # Verify individual getters
        self.assertEqual(r.size, 98)
        self.assertEqual(r.x, 102)
        self.assertEqual(r.y, 103)

    # ----------------- Validation Tests ------------------------

    def invalid_types(self):
        '''Returns a tuple of invalid types for testing.'''
        return (3.14, -1.1, float('inf'), float('-inf'), True, "str",
                (2,), [4], {5}, {6: 7}, None)

    def test_G_validate_type(self):
        '''Tests type validation for Square properties.'''
        r = Square(1)
        for attr in ["x", "y"]:
            msg = f"{attr} must be an integer"
            for invalid in self.invalid_types():
                with self.assertRaises(TypeError) as e:
                    setattr(r, attr, invalid)
                self.assertEqual(str(e.exception), msg)

        # Check width validation
        msg = "width must be an integer"
        for invalid in self.invalid_types():
            with self.assertRaises(TypeError) as e:
                setattr(r, "width", invalid)
            self.assertEqual(str(e.exception), msg)

    def test_G_validate_value_negative_gt(self):
        '''Tests for negative size values.'''
        r = Square(1, 2)
        for attr in ["size"]:
            msg = f"width must be > 0"
            with self.assertRaises(ValueError) as e:
                setattr(r, attr, -(randrange(10) + 1))
            self.assertEqual(str(e.exception), msg)

    def test_G_validate_value_negative_ge(self):
        '''Tests for negative x and y values.'''
        r = Square(1, 2)
        for attr in ["x", "y"]:
            msg = f"{attr} must be >= 0"
            with self.assertRaises(ValueError) as e:
                setattr(r, attr, -(randrange(10) + 1))
            self.assertEqual(str(e.exception), msg)

    # ----------------- Method Tests ------------------------

    def test_H_area(self):
        '''Validates the area computation.'''
        r = Square(5)  # Create a Square with size 5
        self.assertEqual(r.area(), 25)  # Check if area matches expected value

    def test_I_display(self):
        '''Checks display() method output.'''
        r = Square(3)  # Create a 3x3 square
        f = io.StringIO()
        with redirect_stdout(f):
            r.display()  # Capture printed output
        expected_output = "###\n###\n###\n"
        self.assertEqual(f.getvalue(), expected_output)

if __name__ == "__main__":
    unittest.main()  # Run the test suite if executed directly

