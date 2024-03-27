#!/usr/bin/python3
"""
Module for amenity.py
"""
import unittest
from models.state import State
import datetime


class TestState(unittest.TestCase):
    """ Method to test instances and methods from State class """

    j = State()

    def test_class_exists(self):
        """Function to tests if class exists"""
        result = "<class 'models.state.State'>"
        self.assertEqual(str(type(self.j)), result)

    def test_user_inheritance(self):
        """Function to test if this  is a subclass of BaseModel"""
        self.assertIsInstance(self.j, State)

    def testHasAttributes(self):
        """Function to verify if attributes exist"""
        self.assertTrue(hasattr(self.j, 'name'))
        self.assertTrue(hasattr(self.j, 'id'))
        self.assertTrue(hasattr(self.j, 'created_at'))
        self.assertTrue(hasattr(self.j, 'updated_at'))

    def test_types(self):
        """Functionto tests if the type of the verified  attribute is the correct"""
        self.assertIsInstance(self.j.name, str)
        self.assertIsInstance(self.j.id, str)
        self.assertIsInstance(self.j.created_at, datetime.datetime)
        self.assertIsInstance(self.j.updated_at, datetime.datetime)

if __name__ == '__main__':
    unittest.main()
