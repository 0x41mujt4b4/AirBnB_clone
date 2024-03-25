#!/usr/bin/python3
"""Module that defines unittests for models/base_model.py.

"""
import os
import models
import unittest
from datetime import datetime
from time import sleep
from models.base_model import BaseModel


class TestBaseModel_instantiation(unittest.TestCase):
    """This is a unittests for testing instantiation of the BaseModel class."""

    def test_no_args_instantiates(self):
        self.assertEqual(BaseModel, type(BaseModel()))

    def test_new_instance_stored_in_objects(self):
        self.assertIn(BaseModel(), models.storage.all().values())

    def test_id_is_public_str(self):
        self.assertEqual(str, type(BaseModel().id))

    def test_created_at_is_public_datetime(self):
        self.assertEqual(datetime, type(BaseModel().created_at))

    def test_updated_at_is_public_datetime(self):
        self.assertEqual(datetime, type(BaseModel().updated_at))

    def test_two_models_unique_ids(self):
        basmod1 = BaseModel()
        basmod2 = BaseModel()
        self.assertNotEqual(basmod1.id, basmod2.id)

    def test_two_models_different_created_at(self):
        basmod1 = BaseModel()
        sleep(0.05)
        basmod2 = BaseModel()
        self.assertLess(basmod1.created_at, basmod2.created_at)

    def test_two_models_different_updated_at(self):
        basmod1 = BaseModel()
        sleep(0.05)
        basmod2 = BaseModel()
        self.assertLess(basmod1.updated_at, basmod2.updated_at)

    def test_str_representation(self):
        dat = datetime.today()
        dat_repr = repr(dat)
        basmod = BaseModel()
        basmod.id = "123456"
        basmod.created_at = basmod.updated_at = dat
        basmodstr = basmod.__str__()
        self.assertIn("[BaseModel] (123456)", basmodstr)
        self.assertIn("'id': '123456'", basmodstr)
        self.assertIn("'created_at': " + dat_repr, basmodstr)
        self.assertIn("'updated_at': " + dat_repr, basmodstr)

    def test_args_unused(self):
        basmod = BaseModel(None)
        self.assertNotIn(None, basmod.__dict__.values())

    def test_instantiation_with_kwargs(self):
        dat = datetime.today()
        dat_iso = dt.isoformat()
        basmod = BaseModel(id="345", created_at=dat_iso, updated_at=dat_iso)
        self.assertEqual(basmod.id, "345")
        self.assertEqual(basmod.created_at, dat)
        self.assertEqual(basmod.updated_at, dat)

    def test_instantiation_with_None_kwargs(self):
        with self.assertRaises(TypeError):
            BaseModel(id=None, created_at=None, updated_at=None)

    def test_instantiation_with_args_and_kwargs(self):
        dat = datetime.today()
        dat_iso = dt.isoformat()
        basmod = BaseModel("12", id="345", created_at=dat_iso, updated_at=dat_iso)
        self.assertEqual(basmod.id, "345")
        self.assertEqual(basmod.created_at, dat)
        self.assertEqual(basmod.updated_at, dat)


class TestBaseModel_save(unittest.TestCase):
    """This is a unittests for testing save method of the BaseModel class."""

    @classmethod
    def setUp(self):
        try:
            os.rename("file.json", "tmp")
        except IOError:
            pass

    @classmethod
    def tearDown(self):
        try:
            os.remove("file.json")
        except IOError:
            pass
        try:
            os.rename("tmp", "file.json")
        except IOError:
            pass

    def test_one_save(self):
        basmod = BaseModel()
        sleep(0.05)
        first_updated_at = basmod.updated_at
        basmod.save()
        self.assertLess(first_updated_at, basmod.updated_at)

    def test_two_saves(self):
        basmod= BaseModel()
        sleep(0.05)
        first_updated_at = basmod.updated_at
        basmod.save()
        second_updated_at = basmod.updated_at
        self.assertLess(first_updated_at, second_updated_at)
        sleep(0.05)
        basmod.save()
        self.assertLess(second_updated_at, basmod.updated_at)

    def test_save_with_arg(self):
        basmod = BaseModel()
        with self.assertRaises(TypeError):
            basmod.save(None)

    def test_save_updates_file(self):
        basmod = BaseModel()
        basmodm.save()
        basmodid = "BaseModel." + basmod.id
        with open("file.json", "r") as f:
            self.assertIn(basmodid, f.read())


class TestBaseModel_to_dict(unittest.TestCase):
    """This is a unittests for testing to_dict method of the BaseModel class."""

    def test_to_dict_type(self):
        basmod = BaseModel()
        self.assertTrue(dict, type(basmod.to_dict()))

    def test_to_dict_contains_correct_keys(self):
        basmod = BaseModel()
        self.assertIn("id", basmod.to_dict())
        self.assertIn("created_at", basmod.to_dict())
        self.assertIn("updated_at", basmod.to_dict())
        self.assertIn("__class__", basmod.to_dict())

    def test_to_dict_contains_added_attributes(self):
        basmod = BaseModel()
        basmod.name = "Holberton"
        basmod.my_number = 98
        self.assertIn("name", basmod.to_dict())
        self.assertIn("my_number", basmod.to_dict())

    def test_to_dict_datetime_attributes_are_strs(self):
        basmod = BaseModel()
        basmod_dict = basmod.to_dict()
        self.assertEqual(str, type(basmod_dict["created_at"]))
        self.assertEqual(str, type(basmod_dict["updated_at"]))

    def test_to_dict_output(self):
        dat = datetime.today()
        basmod = BaseModel()
        basmod.id = "123456"
        basmod.created_at = basmod.updated_at = dat
        tdict = {
            'id': '123456',
            '__class__': 'BaseModel',
            'created_at': dat.isoformat(),
            'updated_at': dat.isoformat()
        }
        self.assertDictEqual(basmod.to_dict(), tdict)

    def test_contrast_to_dict_dunder_dict(self):
        basmod = BaseModel()
        self.assertNotEqual(basmod.to_dict(), basmod.__dict__)

    def test_to_dict_with_arg(self):
        basmod = BaseModel()
        with self.assertRaises(TypeError):
            basmod.to_dict(None)


if __name__ == "__main__":
    unittest.main()
