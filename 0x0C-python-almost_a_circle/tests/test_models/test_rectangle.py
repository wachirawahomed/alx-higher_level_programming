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

    def test_constructor_with_invalid_width(self):
        with self.assertRaises(TypeError) as context:
            r = Rectangle("10", 20)
        self.assertEqual(str(context.exception), "width must be an integer")

    def test_constructor_with_invalid_height(self):
        with self.assertRaises(TypeError) as context:
            r = Rectangle(10, "20")
        self.assertEqual(str(context.exception), "height must be an integer")

    def test_constructor_with_negative_width(self):
        with self.assertRaises(ValueError) as context:
            r = Rectangle(-10, 20)
        self.assertEqual(str(context.exception), "width must be > 0")

    def test_constructor_with_negative_height(self):
        with self.assertRaises(ValueError) as context:
            r = Rectangle(10, -20)
        self.assertEqual(str(context.exception), "height must be > 0")

    def test_width_setter_with_invalid_value(self):
        r = Rectangle(10, 20)
        with self.assertRaises(TypeError) as context:
            r.width = "30"
        self.assertEqual(str(context.exception), "width must be an integer")

    def test_height_setter_with_invalid_value(self):
        r = Rectangle(10, 20)
        with self.assertRaises(TypeError) as context:
            r.height = "25"
        self.assertEqual(str(context.exception), "height must be an integer")

    def test_x_setter_with_invalid_value(self):
        r = Rectangle(10, 20)
        with self.assertRaises(TypeError) as context:
            r.x = {}
        self.assertEqual(str(context.exception), "x must be an integer")

    def test_y_setter_with_invalid_value(self):
        r = Rectangle(10, 20)
        with self.assertRaises(TypeError) as context:
            r.y = []
        self.assertEqual(str(context.exception), "y must be an integer")

    def test_x_setter_with_negative_value(self):
        r = Rectangle(10, 20)
        with self.assertRaises(ValueError) as context:
            r.x = -5
        self.assertEqual(str(context.exception), "x must be >= 0")

    def test_y_setter_with_negative_value(self):
        r = Rectangle(10, 20)
        with self.assertRaises(ValueError) as context:
            r.y = -10
        self.assertEqual(str(context.exception), "y must be >= 0")

    def test_inheritance_from_base(self):
        self.assertTrue(issubclass(Rectangle, Base))

    def test_area_method(self):
        r1 = Rectangle(3, 2)
        self.assertEqual(r1.area(), 6)

        r2 = Rectangle(2, 10)
        self.assertEqual(r2.area(), 20)

        r3 = Rectangle(8, 7, 0, 0, 12)
        self.assertEqual(r3.area(), 56)

    def test_pep8_compliance(self):
        # Ensure that the Rectangle class implementation follows PEP 8 guidelines
        # You can use a PEP 8 linting tool for this test
        pass  # Placeholder for now

    def test_documentation(self):
        # Ensure that all classes, methods, and functions in the Rectangle class are documented properly
        pass  # Placeholder for now

if __name__ == '__main__':
    unittest.main()

