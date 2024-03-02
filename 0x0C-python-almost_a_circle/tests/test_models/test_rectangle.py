#!/usr/bin/python3
import unittest
from models.rectangle import Rectangle
from models.base import Base

class TestRectangle(unittest.TestCase):

    def test_constructor_with_arguments(self):
        r = Rectangle(10, 20, 5, 10, 1)
        self.assertEqual(r.width, 10)
        self.assertEqual(r.height, 20)
        self.assertEqual(r.x, 5)
        self.assertEqual(r.y, 10)
        self.assertEqual(r.id, 1)

    def test_constructor_default_values(self):
        r = Rectangle(10, 20)
        self.assertEqual(r.x, 0)
        self.assertEqual(r.y, 0)

    def test_width_setter(self):
        r = Rectangle(10, 20)
        r.width = 30
        self.assertEqual(r.width, 30)

    def test_height_setter(self):
        r = Rectangle(10, 20)
        r.height = 25
        self.assertEqual(r.height, 25)

    # Add more tests for x, y setters and getters, area, perimeter, etc.

    def test_inheritance_from_base(self):
        self.assertTrue(issubclass(Rectangle, Base))

    def test_pep8_compliance(self):
        # Ensure that the Rectangle class implementation follows PEP 8 guidelines
        # You can use a PEP 8 linting tool for this test
        pass  # Placeholder for now

    def test_documentation(self):
        # Ensure that all classes, methods, and functions in the Rectangle class are documented properly
        pass  # Placeholder for now

if __name__ == '__main__':
    unittest.main()

