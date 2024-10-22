#!/usr/bin/python3
"""Unit tests for the Square class."""
import unittest
from models.base import Base
from models.square import Square
from random import randrange
from contextlib import redirect_stdout
import io


class TestSquare(unittest.TestCase):
    """Test suite for the Square class."""

    def setUp(self):
        """Resets object counter before each test."""
        Base._Base__nb_objects = 0

    def tearDown(self):
        """Runs after each test to clean up if necessary."""
        pass

    # ----------- Basic Class and Constructor Tests -------------

    def test_A_class(self):
        """Verifies Square class type."""
        self.assertEqual(str(Square), "<class 'models.square.Square'>")

    def test_B_inheritance(self):
        """Checks if Square inherits from Base."""
        self.assertTrue(issubclass(Square, Base))

    def test_C_constructor_no_args(self):
        """Ensures an error is raised without required arguments."""
        with self.assertRaises(TypeError) as e:
            Square()
        self.assertEqual(str(e.exception), 
                         "__init__() missing 1 required positional argument: 'size'")

    def test_C_constructor_many_args(self):
        """Checks constructor with too many arguments."""
        with self.assertRaises(TypeError) as e:
            Square(1, 2, 3, 4, 5)
        self.assertEqual(str(e.exception), 
                         "__init__() takes from 2 to 5 positional arguments but 6 were given")

    def test_D_instantiation(self):
        """Tests correct instantiation of Square objects."""
        r = Square(10)
        self.assertEqual(str(type(r)), "<class 'models.square.Square'>")
        self.assertTrue(isinstance(r, Base))
        expected_dict = {
            '_Rectangle__height': 10, 
            '_Rectangle__width': 10,
            '_Rectangle__x': 0, 
            '_Rectangle__y': 0, 
            'id': 1
        }
        self.assertDictEqual(r.__dict__, expected_dict)

        with self.assertRaises(TypeError) as e:
            Square("1")
        self.assertEqual(str(e.exception), "width must be an integer")

    def test_D_instantiation_positional(self):
        """Validates instantiation using positional arguments."""
        r = Square(5, 10, 15)
        expected_dict = {
            '_Rectangle__height': 5, 
            '_Rectangle__width': 5,
            '_Rectangle__x': 10, 
            '_Rectangle__y': 15, 
            'id': 1
        }
        self.assertEqual(r.__dict__, expected_dict)

    def test_D_instantiation_keyword(self):
        """Validates instantiation with keyword arguments."""
        r = Square(100, id=421, y=99, x=101)
        expected_dict = {
            '_Rectangle__height': 100, 
            '_Rectangle__width': 100,
            '_Rectangle__x': 101, 
            '_Rectangle__y': 99, 
            'id': 421
        }
        self.assertEqual(r.__dict__, expected_dict)

    # ----------- Property Tests -------------

    def test_F_properties(self):
        """Tests getter and setter methods."""
        r = Square(5, 9)
        r.size = 98
        r.x = 102
        r.y = 103
        expected_dict = {
            '_Rectangle__height': 98, 
            '_Rectangle__width': 98,
            '_Rectangle__x': 102, 
            '_Rectangle__y': 103, 
            'id': 1
        }
        self.assertEqual(r.__dict__, expected_dict)

    def test_G_validate_type(self):
        """Validates attribute types."""
        r = Square(1)
        for attr in ["x", "y"]:
            for invalid in self.invalid_types():
                with self.assertRaises(TypeError) as e:
                    setattr(r, attr, invalid)
                self.assertEqual(str(e.exception), f"{attr} must be an integer")

    def invalid_types(self):
        """Provides invalid types for testing."""
        return (3.14, -1.1, float('inf'), float('-inf'), True, "str", (2,), [4], {5}, {6: 7}, None)

    def test_G_validate_value_negative_gt(self):
        """Validates value constraints (greater than zero)."""
        r = Square(1, 2)
        with self.assertRaises(ValueError) as e:
            r.size = -1
        self.assertEqual(str(e.exception), "width must be > 0")

    def test_G_validate_value_zero(self):
        """Checks for size equal to zero."""
        r = Square(1)
        with self.assertRaises(ValueError) as e:
            r.size = 0
        self.assertEqual(str(e.exception), "width must be > 0")

    # ----------- Method Tests -------------

    def test_I_area(self):
        """Verifies the area calculation."""
        r = Square(6)
        self.assertEqual(r.area(), 36)

    def test_J_display_simple(self):
        """Checks display output."""
        r = Square(1)
        f = io.StringIO()
        with redirect_stdout(f):
            r.display()
        self.assertEqual(f.getvalue(), "#\n")

    def test_K_str(self):
        """Tests the __str__() method output."""
        r = Square(3, 4, 5)
        self.assertEqual(str(r), "[Square] (3) 4/5 - 3")

    def test_L_update_args(self):
        """Validates update() method with positional arguments."""
        r = Square(5, 2)
        r.update(10, 7, 3, 4)
        expected = "[Square] (10) 3/4 - 7"
        self.assertEqual(str(r), expected)

    def test_L_update_kwargs(self):
        """Validates update() method with keyword arguments."""
        r = Square(5, 2)
        r.update(size=10, id=1, x=8)
        expected_dict = {
            '_Rectangle__height': 10, 
            '_Rectangle__width': 10,
            '_Rectangle__x': 8, 
            '_Rectangle__y': 0, 
            'id': 1
        }
        self.assertEqual(r.__dict__, expected_dict)

    def test_M_to_dictionary(self):
        """Checks to_dictionary() method."""
        r = Square(9, 2, 3, 4)
        expected = {'x': 2, 'y': 3, 'size': 9, 'id': 4}
        self.assertEqual(r.to_dictionary(), expected)


if __name__ == "__main__":
    unittest.main()

