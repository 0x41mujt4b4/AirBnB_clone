#!/usr/bin/python3
"""
Unittest for amenity.py
"""
import unittest
from models.place import Place
import datetime


class TestPlace(unittest.TestCase):
    """Class to tests instances and methods from amenity class"""

    i = Place()

    def test_class_exists(self):
        """Function to tests if class exists"""
        self.assertEqual(str(type(self.i)), "<class 'models.place.Place'>")

    def test_user_inheritance(self):
        """Function to test if this  is a subclass of BaseModel"""
        self.assertIsInstance(self.i, Place)

    def testHasAttributes(self):
        """Function to confirm if attributes exist"""
        self.assertTrue(hasattr(self.i, 'city_id'))
        self.assertTrue(hasattr(self.i, 'user_id'))
        self.assertTrue(hasattr(self.i, 'name'))
        self.assertTrue(hasattr(self.i, 'description'))
        self.assertTrue(hasattr(self.i, 'number_rooms'))
        self.assertTrue(hasattr(self.i, 'number_bathrooms'))
        self.assertTrue(hasattr(self.i, 'max_guest'))
        self.assertTrue(hasattr(self.i, 'price_by_night'))
        self.assertTrue(hasattr(self.i, 'latitude'))
        self.assertTrue(hasattr(self.i, 'longitude'))
        self.assertTrue(hasattr(self.i, 'amenity_ids'))
        self.assertTrue(hasattr(self.i, 'id'))
        self.assertTrue(hasattr(self.i, 'created_at'))
        self.assertTrue(hasattr(self.i, 'updated_at'))

    def test_types(self):
        """Function to tests if the type of the verified attribute is the correct"""
        self.assertIsInstance(self.i.city_id, str)
        self.assertIsInstance(self.i.user_id, str)
        self.assertIsInstance(self.i.name, str)
        self.assertIsInstance(self.i.description, str)
        self.assertIsInstance(self.i.number_rooms, int)
        self.assertIsInstance(self.i.number_bathrooms, int)
        self.assertIsInstance(self.i.max_guest, int)
        self.assertIsInstance(self.i.price_by_night, int)
        self.assertIsInstance(self.i.latitude, float)
        self.assertIsInstance(self.i.longitude, float)
        self.assertIsInstance(self.i.amenity_ids, list)
        self.assertIsInstance(self.i.id, str)
        self.assertIsInstance(self.i.created_at, datetime.datetime)
        self.assertIsInstance(self.i.updated_at, datetime.datetime)

if __name__ == '__main__':
    unittest.main()
