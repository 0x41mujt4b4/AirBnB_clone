#!/usr/bin/python3
"""
Module for review.py
"""
import unittest
from models.review import Review
import datetime


class TestReview(unittest.TestCase):
    """Function to tests instances and methods from Review class"""

    x = Review()

    def test_class_exists(self):
        """Function to tests if class exists"""
        result = "<class 'models.review.Review'>"
        self.assertEqual(str(type(self.x)), result)

    def test_user_inheritance(self):
        """Function to test if Review is a subclass of BaseModel"""
        self.assertIsInstance(self.x, Review)

    def testHasAttributes(self):
        """Function to verify if attributes exist"""
        self.assertTrue(hasattr(self.x, 'place_id'))
        self.assertTrue(hasattr(self.x, 'user_id'))
        self.assertTrue(hasattr(self.x, 'text'))
        self.assertTrue(hasattr(self.x, 'id'))
        self.assertTrue(hasattr(self.x, 'created_at'))
        self.assertTrue(hasattr(self.x, 'updated_at'))

    def test_types(self):
        """Function to tests if the type of the verified attribute is the correct"""
        self.assertIsInstance(self.x.place_id, str)
        self.assertIsInstance(self.x.user_id, str)
        self.assertIsInstance(self.x.text, str)
        self.assertIsInstance(self.x.id, str)
        self.assertIsInstance(self.x.created_at, datetime.datetime)
        self.assertIsInstance(self.x.updated_at, datetime.datetime)
