#!/usr/bin/python3
"""Unittest for Square class"""
import unittest
from models.square import Square
from models.rectangle import Rectangle
from models.base import Base
import io
import sys


class TestSquare(unittest.TestCase):
    """Test cases for Square class"""

    def setUp(self):
        """Reset Base._nb_objects before each test"""
        Base._Base__nb_objects = 0

    def test_square_is_base(self):
        """Test if Square is an instance of Base"""
        self.assertIsInstance(Square(10), Base)

    def test_square_is_rectangle(self):
        """Test if Square is an instance of Rectangle"""
        self.assertIsInstance(Square(10), Rectangle)

    def test_no_args(self):
        """Test Square with no arguments"""
        with self.assertRaises(TypeError):
            Square()

    def test_one_arg(self):
        """Test Square with one argument"""
        s1 = Square(10)
        s2 = Square(11)
        self.assertEqual(s1.id, s2.id - 1)

    def test_two_args(self):
        """Test Square with two arguments"""
        s1 = Square(10, 2)
        s2 = Square(2, 10)
        self.assertEqual(s1.id, s2.id - 1)

    def test_three_args(self):
        """Test Square with three arguments"""
        s1 = Square(10, 2, 2)
        s2 = Square(2, 2, 10)
        self.assertEqual(s1.id, s2.id - 1)

    def test_four_args(self):
        """Test Square with four arguments"""
        self.assertEqual(7, Square(10, 2, 2, 7).id)

    def test_more_than_four_args(self):
        """Test Square with more than four arguments"""
        with self.assertRaises(TypeError):
            Square(1, 2, 3, 4, 5)

    def test_size_private(self):
        """Test if size is private"""
        with self.assertRaises(AttributeError):
            print(Square(10, 2, 3, 4).__size)

    def test_size_getter(self):
        """Test size getter"""
        self.assertEqual(5, Square(5, 2, 3, 9).size)

    def test_size_setter(self):
        """Test size setter"""
        s = Square(4, 1, 9, 2)
        s.size = 8
        self.assertEqual(8, s.size)

    def test_width_getter(self):
        """Test width getter"""
        s = Square(4, 1, 9, 2)
        s.size = 8
        self.assertEqual(8, s.width)

    def test_height_getter(self):
        """Test height getter"""
        s = Square(4, 1, 9, 2)
        s.size = 8
        self.assertEqual(8, s.height)

    def test_x_getter(self):
        """Test x getter"""
        self.assertEqual(0, Square(10).x)

    def test_y_getter(self):
        """Test y getter"""
        self.assertEqual(0, Square(10).y)

    def test_invalid_size_type(self):
        """Test invalid size type"""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square("invalid")

    def test_invalid_size_value(self):
        """Test invalid size value"""
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Square(-10)

    def test_invalid_x_type(self):
        """Test invalid x type"""
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(10, "invalid")

    def test_invalid_y_type(self):
        """Test invalid y type"""
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(10, 2, "invalid")

    def test_invalid_x_value(self):
        """Test invalid x value"""
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            Square(10, -2)

    def test_invalid_y_value(self):
        """Test invalid y value"""
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            Square(10, 2, -3)

    def test_area(self):
        """Test area calculation"""
        self.assertEqual(100, Square(10, 2, 3, 4).area())

    def test_display_without_xy(self):
        """Test display method without x and y"""
        s = Square(2)
        expected_output = "##\n##\n"
        captured_output = io.StringIO()
        sys.stdout = captured_output
        s.display()
        sys.stdout = sys.__stdout__
        self.assertEqual(expected_output, captured_output.getvalue())

    def test_display_with_xy(self):
        """Test display method with x and y"""
        s = Square(2, 2, 2)
        expected_output = "\n\n  ##\n  ##\n"
        captured_output = io.StringIO()
        sys.stdout = captured_output
        s.display()
        sys.stdout = sys.__stdout__
        self.assertEqual(expected_output, captured_output.getvalue())

    def test_str(self):
        """Test __str__ method"""
        s = Square(4, 2, 1, 12)
        expected = "[Square] (12) 2/1 - 4"
        self.assertEqual(expected, str(s))

    def test_update_args(self):
        """Test update method with *args"""
        s = Square(10, 10, 10, 10)
        s.update(89, 2, 3, 4)
        self.assertEqual("[Square] (89) 3/4 - 2", str(s))

    def test_update_kwargs(self):
        """Test update method with **kwargs"""
        s = Square(10, 10, 10, 10)
        s.update(size=1, x=2, y=3, id=89)
        self.assertEqual("[Square] (89) 2/3 - 1", str(s))

    def test_to_dictionary(self):
        """Test to_dictionary method"""
        s = Square(10, 2, 1, 1)
        expected = {'id': 1, 'size': 10, 'x': 2, 'y': 1}
        self.assertDictEqual(expected, s.to_dictionary())


if __name__ == "__main__":
    unittest.main()
