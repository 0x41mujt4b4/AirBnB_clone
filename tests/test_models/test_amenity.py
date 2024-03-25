#!/usr/bin/python3
"""
This is a unittest for amenity.py file
"""
import unittest
from models.amenity import Amenity
import datetime


class TestAmenity(unittest.TestCase):
    """Is a class function to tests instances and methods from amenity class"""

    i = Amenity()

    def test_class_exists(self):
        """Is a function to test if class do exists"""
        result = "<class 'models.amenity.Amenity'>"
        self.assertEqual(str(type(self.i)), result)

    def test_user_inheritance(self):
        """Is a function to see if Amenity is a subclass of BaseModel"""
        self.assertIsInstance(self.i, Amenity)

    def testHasAttributes(self):
        """Function to confirm if attributes exist"""
        self.assertTrue(hasattr(self.i, 'name'))
        self.assertTrue(hasattr(self.i, 'id'))
        self.assertTrue(hasattr(self.i, 'created_at'))
        self.assertTrue(hasattr(self.i, 'updated_at'))

    def test_types(self):
        """This is a function to tests if the type of the given  attribute is indeed correct"""
        self.assertIsInstance(self.i.name, str)
        self.assertIsInstance(self.i.id, str)
        self.assertIsInstance(self.i.created_at, datetime.datetime)
        self.assertIsInstance(self.i.updated_at, datetime.datetime)

if __name__ == '__main__':
    unittest.main()
