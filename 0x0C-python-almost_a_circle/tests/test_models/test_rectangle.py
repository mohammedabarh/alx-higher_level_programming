#!/usr/bin/python3
"""Unittest for Rectangle class"""
import unittest
from models.rectangle import Rectangle
from models.base import Base
import io
import sys


class TestRectangle(unittest.TestCase):
    """Test cases for Rectangle class"""

    def setUp(self):
        """Reset Base._nb_objects before each test"""
        Base._Base__nb_objects = 0

    def test_rectangle_is_base(self):
        """Test if Rectangle is an instance of Base"""
        self.assertIsInstance(Rectangle(10, 2), Base)

    def test_no_args(self):
        """Test Rectangle with no arguments"""
        with self.assertRaises(TypeError):
            Rectangle()

    def test_one_arg(self):
        """Test Rectangle with one argument"""
        with self.assertRaises(TypeError):
            Rectangle(1)

    def test_two_args(self):
        """Test Rectangle with two arguments"""
        r1 = Rectangle(10, 2)
        r2 = Rectangle(2, 10)
        self.assertEqual(r1.id, r2.id - 1)

    def test_three_args(self):
        """Test Rectangle with three arguments"""
        r1 = Rectangle(2, 2, 4)
        r2 = Rectangle(4, 4, 2)
        self.assertEqual(r1.id, r2.id - 1)

    def test_four_args(self):
        """Test Rectangle with four arguments"""
        r1 = Rectangle(1, 2, 3, 4)
        r2 = Rectangle(4, 3, 2, 1)
        self.assertEqual(r1.id, r2.id - 1)

    def test_five_args(self):
        """Test Rectangle with five arguments"""
        self.assertEqual(7, Rectangle(10, 2, 0, 0, 7).id)

    def test_more_than_five_args(self):
        """Test Rectangle with more than five arguments"""
        with self.assertRaises(TypeError):
            Rectangle(1, 2, 3, 4, 5, 6)

    def test_width_private(self):
        """Test if width is private"""
        with self.assertRaises(AttributeError):
            print(Rectangle(5, 5, 0, 0, 1).__width)

    def test_height_private(self):
        """Test if height is private"""
        with self.assertRaises(AttributeError):
            print(Rectangle(5, 5, 0, 0, 1).__height)

    def test_x_private(self):
        """Test if x is private"""
        with self.assertRaises(AttributeError):
            print(Rectangle(5, 5, 0, 0, 1).__x)

    def test_y_private(self):
        """Test if y is private"""
        with self.assertRaises(AttributeError):
            print(Rectangle(5, 5, 0, 0, 1).__y)

    def test_width_getter(self):
        """Test width getter"""
        r = Rectangle(5, 7, 7, 5, 1)
        self.assertEqual(5, r.width)

    def test_width_setter(self):
        """Test width setter"""
        r = Rectangle(5, 7, 7, 5, 1)
        r.width = 10
        self.assertEqual(10, r.width)

    def test_height_getter(self):
        """Test height getter"""
        r = Rectangle(5, 7, 7, 5, 1)
        self.assertEqual(7, r.height)

    def test_height_setter(self):
        """Test height setter"""
        r = Rectangle(5, 7, 7, 5, 1)
        r.height = 10
        self.assertEqual(10, r.height)

    def test_x_getter(self):
        """Test x getter"""
        r = Rectangle(5, 7, 7, 5, 1)
        self.assertEqual(7, r.x)

    def test_x_setter(self):
        """Test x setter"""
        r = Rectangle(5, 7, 7, 5, 1)
        r.x = 10
        self.assertEqual(10, r.x)

    def test_y_getter(self):
        """Test y getter"""
        r = Rectangle(5, 7, 7, 5, 1)
        self.assertEqual(5, r.y)

    def test_y_setter(self):
        """Test y setter"""
        r = Rectangle(5, 7, 7, 5, 1)
        r.y = 10
        self.assertEqual(10, r.y)

    def test_invalid_width_type(self):
        """Test invalid width type"""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle("invalid", 2)

    def test_invalid_height_type(self):
        """Test invalid height type"""
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(2, "invalid")

    def test_invalid_x_type(self):
        """Test invalid x type"""
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(1, 2, "invalid", 2)

    def test_invalid_y_type(self):
        """Test invalid y type"""
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(1, 2, 2, "invalid")

    def test_invalid_width_value(self):
        """Test invalid width value"""
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Rectangle(-1, 2)

    def test_invalid_height_value(self):
        """Test invalid height value"""
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            Rectangle(1, -2)

    def test_invalid_x_value(self):
        """Test invalid x value"""
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            Rectangle(1, 2, -1, 2)

    def test_invalid_y_value(self):
        """Test invalid y value"""
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            Rectangle(1, 2, 2, -1)

    def test_area(self):
        """Test area calculation"""
        r = Rectangle(3, 2)
        self.assertEqual(6, r.area())

    def test_area_large(self):
        """Test area calculation with large numbers"""
        r = Rectangle(999999999999999, 999999999999999999)
        self.assertEqual(999999999999998999000000000000001, r.area())

    def test_display(self):
        """Test display method"""
        r = Rectangle(2, 3, 2, 2)
        expected_output = "\n\n  ##\n  ##\n  ##\n"
        captured_output = io.StringIO()
        sys.stdout = captured_output
        r.display()
        sys.stdout = sys.__stdout__
        self.assertEqual(expected_output, captured_output.getvalue())

    def test_str(self):
        """Test __str__ method"""
        r = Rectangle(4, 6, 2, 1, 12)
        expected = "[Rectangle] (12) 2/1 - 4/6"
        self.assertEqual(expected, str(r))

    def test_update_args(self):
        """Test update method with *args"""
        r = Rectangle(10, 10, 10, 10)
        r.update(89, 2, 3, 4, 5)
        self.assertEqual("[Rectangle] (89) 4/5 - 2/3", str(r))

    def test_update_kwargs(self):
        """Test update method with **kwargs"""
        r = Rectangle(10, 10, 10, 10)
        r.update(height=1, width=2, y=3, x=4, id=89)
        self.assertEqual("[Rectangle] (89) 4/3 - 2/1", str(r))

    def test_to_dictionary(self):
        """Test to_dictionary method"""
        r = Rectangle(10, 2, 1, 9, 1)
        expected = {'id': 1, 'width': 10, 'height': 2, 'x': 1, 'y': 9}
        self.assertDictEqual(expected, r.to_dictionary())


if __name__ == "__main__":
    unittest.main()
