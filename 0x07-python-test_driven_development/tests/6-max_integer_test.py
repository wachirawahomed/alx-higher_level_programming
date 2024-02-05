#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    """Test cases for the max_integer function"""

    def test_regular_list(self):
        """Test when the list is in ascending order."""
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_reverse_sorted_list(self):
        """Test when the list is in descending order."""
        self.assertEqual(max_integer([4, 3, 2, 1]), 4)

    def test_unsorted_list(self):
        """Test when the list is unsorted."""
        self.assertEqual(max_integer([1, 3, 4, 2]), 4)

    def test_empty_list(self):
        """Test when the list is empty."""
        self.assertIsNone(max_integer([]))

    def test_single_element_list(self):
        """Test when the list has only one element."""
        self.assertEqual(max_integer([5]), 5)

    def test_negative_numbers_list(self):
        """Test when the list contains only negative numbers."""
        self.assertEqual(max_integer([-1, -5, -3, -2]), -1)

    def test_mixed_numbers_list(self):
        """Test when the list contains mixed positive and negative numbers."""
        self.assertEqual(max_integer([-1, 5, 0, -2]), 5)

    def test_type_error_non_list(self):
        """Test if a TypeError is raised when input is not a list."""
        with self.assertRaises(TypeError):
            max_integer(123)
