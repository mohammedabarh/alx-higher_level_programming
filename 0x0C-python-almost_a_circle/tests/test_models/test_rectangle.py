#!/usr/bin/python3
"""Unit tests for the Rectangle class."""
import unittest
from models.base import Base
from models.rectangle import Rectangle
from random import randrange
from contextlib import redirect_stdout
import io


class TestRectangle(unittest.TestCase):
    """Test suite for the Rectangle class."""

    def setUp(self):
        """Reset the number of Base objects before each test."""
        Base._Base__nb_objects = 0

    def tearDown(self):
        """Clean up actions after each test."""
        pass

    # ----------------- Tests for Rectangle class structure ------------------------

    def test_A_class(self):
        """Verify the Rectangle class type."""
        self.assertEqual(str(Rectangle),
                         "<class 'models.rectangle.Rectangle'>")

    def test_B_inheritance(self):
        """Check if Rectangle is a subclass of Base."""
        self.assertTrue(issubclass(Rectangle, Base))

    def test_C_constructor_no_args(self):
        """Ensure constructor raises an error with missing arguments."""
        with self.assertRaises(TypeError) as e:
            Rectangle()
        expected = "__init__() missing 2 required positional arguments: 'width' and 'height'"
        self.assertEqual(str(e.exception), expected)

    def test_C_constructor_many_args(self):
        """Ensure constructor raises an error with too many arguments."""
        with self.assertRaises(TypeError) as e:
            Rectangle(1, 2, 3, 4, 5, 6)
        expected = "__init__() takes from 3 to 6 positional arguments but 7 were given"
        self.assertEqual(str(e.exception), expected)

    def test_C_constructor_one_arg(self):
        """Ensure constructor raises an error with only one argument."""
        with self.assertRaises(TypeError) as e:
            Rectangle(1)
        expected = "__init__() missing 1 required positional argument: 'height'"
        self.assertEqual(str(e.exception), expected)

    # ----------------- Instantiation tests ------------------------

    def test_D_instantiation(self):
        """Test Rectangle instantiation with valid and invalid values."""
        r = Rectangle(10, 20)
        self.assertEqual(str(type(r)), "<class 'models.rectangle.Rectangle'>")
        self.assertTrue(isinstance(r, Base))
        expected_dict = {
            '_Rectangle__height': 20, '_Rectangle__width': 10,
            '_Rectangle__x': 0, '_Rectangle__y': 0, 'id': 1
        }
        self.assertDictEqual(r.__dict__, expected_dict)

        # Test invalid types
        with self.assertRaises(TypeError) as e:
            Rectangle("1", 2)
        self.assertEqual(str(e.exception), "width must be an integer")

        with self.assertRaises(TypeError) as e:
            Rectangle(1, "2")
        self.assertEqual(str(e.exception), "height must be an integer")

        # Test invalid values
        with self.assertRaises(ValueError) as e:
            Rectangle(-1, 2)
        self.assertEqual(str(e.exception), "width must be > 0")

        with self.assertRaises(ValueError) as e:
            Rectangle(1, -2)
        self.assertEqual(str(e.exception), "height must be > 0")

    def test_D_instantiation_positional(self):
        """Test Rectangle instantiation with positional arguments."""
        r = Rectangle(5, 10, 15, 20)
        expected_dict = {
            '_Rectangle__height': 10, '_Rectangle__width': 5,
            '_Rectangle__x': 15, '_Rectangle__y': 20, 'id': 1
        }
        self.assertEqual(r.__dict__, expected_dict)

    def test_D_instantiation_keyword(self):
        """Test Rectangle instantiation with keyword arguments."""
        r = Rectangle(100, 200, id=421, y=99, x=101)
        expected_dict = {
            '_Rectangle__height': 200, '_Rectangle__width': 100,
            '_Rectangle__x': 101, '_Rectangle__y': 99, 'id': 421
        }
        self.assertEqual(r.__dict__, expected_dict)

    def test_E_id_inherited(self):
        """Verify id inheritance from the Base class."""
        Base._Base__nb_objects = 98
        r = Rectangle(2, 4)
        self.assertEqual(r.id, 99)

    # ----------------- Property validation tests ------------------------

    def test_F_properties(self):
        """Test the getters and setters of Rectangle properties."""
        r = Rectangle(5, 9)
        r.width = 100
        r.height = 101
        r.x = 102
        r.y = 103
        expected_dict = {
            '_Rectangle__height': 101, '_Rectangle__width': 100,
            '_Rectangle__x': 102, '_Rectangle__y': 103, 'id': 1
        }
        self.assertEqual(r.__dict__, expected_dict)

    def test_G_validate_type(self):
        """Test validation for property types."""
        r = Rectangle(1, 2)
        invalid_values = (3.14, "str", (2,), [4], {5}, None)
        for attr in ["x", "y", "width", "height"]:
            for value in invalid_values:
                with self.assertRaises(TypeError) as e:
                    setattr(r, attr, value)
                self.assertIn(f"{attr} must be an integer", str(e.exception))

    def test_G_validate_value_negative(self):
        """Test validation for negative property values."""
        r = Rectangle(1, 2)
        for attr in ["width", "height"]:
            with self.assertRaises(ValueError) as e:
                setattr(r, attr, -1)
            self.assertIn(f"{attr} must be > 0", str(e.exception))

    # ----------------- Area and display method tests ------------------------

    def test_I_area(self):
        """Test the area() method."""
        r = Rectangle(5, 6)
        self.assertEqual(r.area(), 30)

    def test_J_display_simple(self):
        """Test display() method output."""
        r = Rectangle(3, 2)
        f = io.StringIO()
        with redirect_stdout(f):
            r.display()
        expected_output = "###\n###\n"
        self.assertEqual(f.getvalue(), expected_output)

    # ----------------- __str__ and update method tests ------------------------

    def test_K_str(self):
        """Test the __str__() method."""
        r = Rectangle(3, 4, 5, 6)
        self.assertEqual(str(r), "[Rectangle] (1) 5/6 - 3/4")

    def test_L_update_args(self):
        """Test the update() method with positional arguments."""
        r = Rectangle(5, 2)
        r.update(10, 8, 7, 6, 5)
        expected_dict = {
            '_Rectangle__width': 8, '_Rectangle__height': 7,
            '_Rectangle__x': 6, '_Rectangle__y': 5, 'id': 10
        }
        self.assertEqual(r.__dict__, expected_dict)

    def test_L_update_kwargs(self):
        """Test the update() method with keyword arguments."""
        r = Rectangle(5, 2)
        r.update(width=8, height=7, x=6, y=5, id=10)
        expected_dict = {
            '_Rectangle__width': 8, '_Rectangle__height': 7,
            '_Rectangle__x': 6, '_Rectangle__y': 5, 'id': 10
        }
        self.assertEqual(r.__dict__, expected_dict)

# Run the test cases if the script is executed directly
if __name__ == "__main__":
    unittest.main()

