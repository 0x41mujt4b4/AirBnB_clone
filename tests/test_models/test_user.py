#!/usr/bin/python3
"""
Module for user.py
"""
import unittest
from models.user import User
import datetime


class UserCase(unittest.TestCase):
    """Function to tests instances and methods from user class"""

    x = User()

    def test_class_exists(self):
        """Function to tests if class exists"""
        self.assertEqual(str(type(self.x)), "<class 'models.user.User'>")

    def test_user_inheritance(self):
        """Function to test if User is a subclass of BaseModel"""
        self.assertIsInstance(self.x, User)

    def testHasAttributes(self):
        """Function to verify if attributes exist"""
        self.assertTrue(hasattr(self.x, 'email'))
        self.assertTrue(hasattr(self.x, 'password'))
        self.assertTrue(hasattr(self.x, 'first_name'))
        self.assertTrue(hasattr(self.x, 'last_name'))
        self.assertTrue(hasattr(self.x, 'id'))
        self.assertTrue(hasattr(self.x, 'created_at'))
        self.assertTrue(hasattr(self.x, 'updated_at'))

    def test_types(self):
        """Function to tests if the type of the verified  attribute is the correct"""
        self.assertIsInstance(self.x.first_name, str)
        self.assertIsInstance(self.x.last_name, str)
        self.assertIsInstance(self.x.email, str)
        self.assertIsInstance(self.x.password, str)
        self.assertIsInstance(self.x.id, str)
        self.assertIsInstance(self.x.created_at, datetime.datetime)
        self.assertIsInstance(self.x.updated_at, datetime.datetime)

if __name__ == '__main__':
    unittest.main()
