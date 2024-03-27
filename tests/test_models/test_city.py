#!/usr/bin/python3
"""
Module for user.py
"""
import unittest
from models.city import City
import datetime


class TestCity(unittest.TestCase):
    """Function to tests instances and methods om this class"""

    x = City()

    def test_class_exists(self):
        """Function to tests if class exists"""
        self.assertEqual(str(type(self.x)), "<class 'models.city.City'>")

    def test_user_inheritance(self):
        """Function to test if this is a subclass of BaseModel"""
        self.assertTrue(self.x, City)

    def testHasAttributes(self):
        """Function to look if attributes exist"""
        self.assertTrue(hasattr(self.x, 'state_id'))
        self.assertTrue(hasattr(self.x, 'name'))
        self.assertTrue(hasattr(self.x, 'id'))
        self.assertTrue(hasattr(self.x, 'created_at'))
        self.assertTrue(hasattr(self.x, 'updated_at'))

    def test_types(self):
        """Function to tests if the type of the attribute verified is  the correct"""
        self.assertIsInstance(self.x.state_id, str)
        self.assertIsInstance(self.x.name, str)
        self.assertIsInstance(self.x.id, str)
        self.assertIsInstance(self.x.created_at, datetime.datetime)
        self.assertIsInstance(self.x.updated_at, datetime.datetime)

if __name__ == '__main__':
    unittest.main()
