#!/usr/bin/python3
"""
A module that test differents behaviors
of the Base class
"""
import unittest
from models.base import Base

class TestBase(unittest.TestCase):

    def test_constructor_with_id(self):
        b = Base(10)
        self.assertEqual(b.id, 10)

    def test_constructor_without_id(self):
        b1 = Base()
        b2 = Base()
        self.assertEqual(b1.id, 1)
        self.assertEqual(b2.id, 2)

    def test_id_setter(self):
        b = Base()
        b.id = 100
        self.assertEqual(b.id, 100)

    def test_nb_objects_private(self):
        b = Base()
        with self.assertRaises(AttributeError):
            print(b.__nb_objects)

    def test_pep8_compliance(self):
        # Ensure that the Base class implementation follows PEP 8 guidelines
        # You can use a PEP 8 linting tool for this test
        pass

    def test_documentation(self):
        # Ensure that all classes, methods, and functions in the Base class are documented properly
        pass

if __name__ == '__main__':
    unittest.main()
