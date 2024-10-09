#!/usr/bin/python3
"""Unittest for max_integer([..])"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Test cases for the max_integer function"""

    def test_empty_list(self):
        """Test with an empty list"""
        self.assertIsNone(max_integer([]))

    def test_single_element(self):
        """Test with a single element list"""
        self.assertEqual(max_integer([5]), 5)

    def test_positive_numbers(self):
        """Test with positive numbers"""
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)
        self.assertEqual(max_integer([1, 3, 4, 2]), 4)

    def test_negative_numbers(self):
        """Test with negative numbers"""
        self.assertEqual(max_integer([-1, -2, -3, -4]), -1)
        self.assertEqual(max_integer([-1, -3, -4, -2]), -1)

    def test_mixed_numbers(self):
        """Test with mixed positive and negative numbers"""
        self.assertEqual(max_integer([-1, 2, -3, 4]), 4)
        self.assertEqual(max_integer([-1, -2, 3, -4]), 3)

    def test_duplicate_numbers(self):
        """Test with duplicate numbers"""
        self.assertEqual(max_integer([1, 1, 1, 1]), 1)
        self.assertEqual(max_integer([1, 3, 3, 2]), 3)

    def test_floats(self):
        """Test with floating point numbers"""
        self.assertEqual(max_integer([1.5, 2.5, 3.5, 4.5]), 4.5)
        self.assertEqual(max_integer([-1.5, -2.5, -3.5, -4.5]), -1.5)

    def test_ints_and_floats(self):
        """Test with a mix of integers and floats"""
        self.assertEqual(max_integer([1, 2.5, 3, 4.5]), 4.5)

    def test_string(self):
        """Test with a string"""
        self.assertEqual(max_integer("Hello"), 'o')

    def test_list_of_strings(self):
        """Test with a list of strings"""
        self.assertEqual(max_integer(["a", "b", "c", "d"]), 'd')

    def test_empty_string(self):
        """Test with an empty string"""
        self.assertIsNone(max_integer(""))

    def test_large_numbers(self):
        """Test with large numbers"""
        self.assertEqual(max_integer([1000000, 10000000, 100000000]), 100000000)

    def test_bool_values(self):
        """Test with boolean values"""
        self.assertEqual(max_integer([True, False]), True)

    def test_mixed_types(self):
        """Test with mixed types (should raise TypeError)"""
        with self.assertRaises(TypeError):
            max_integer([1, "string", 2, 3])


if __name__ == '__main__':
    unittest.main()
