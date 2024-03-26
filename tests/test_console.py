#!/usr/bin/python3
"""This is a unittest for the FileStorage class.
"""

import unittest
from unittest.mock import patch
from io import StringIO
import json
import os
import pep8
from console import HBNBCommand
from models.engine.file_storage import FileStorage


class TestConsoleClass(unittest.TestCase):
    """
    Class containing unit tests for the HBNBCommand class.
    """
    maxDiff = None

    def setUp(self):
        """
        Function to set test environment by creating a temporary test file.
        """
        with open("test.json", 'w'):
            FileStorage._FileStorage__file_path = "test.json"
            FileStorage._FileStorage__objects = {}

    def tearDown(self):
        """
        Function to  erase the temporary test file.
        """
        FileStorage._FileStorage__file_path = "file.json"
        try:
            os.remove("test.json")
        except FileNotFoundError:
            pass

    def test_module_doc(self):
        """
        Function to check module documentation.
        """
        self.assertTrue(len(HBNBCommand.__doc__) > 0)

    def test_class_doc(self):
        """
        Function to check class documentation.
        """
        self.assertTrue(len(HBNBCommand.__doc__) > 0)

    def test_method_docs(self):
        """
        Function to check  for method documentation.
        """
        for func in dir(HBNBCommand):
            self.assertTrue(len(func.__doc__) > 0)

    def test_pep8(self):
        """
        Function to test for PEP8 conformance in all base files.
        """
        style = pep8.StyleGuide(quiet=True)
        file1 = 'console.py'
        file2 = 'tests/test_console.py'
        result = style.check_files([file1, file2])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warning).")

    def test_executable_file(self):
        """
        Function to check if the file has the necessary permissions to run.
        """
        is_read_true = os.access('console.py', os.R_OK)
        self.assertTrue(is_read_true)
        
        is_write_true = os.access('console.py', os.W_OK)
        self.assertTrue(is_write_true)
        
        is_exec_true = os.access('console.py', os.X_OK)
        self.assertTrue(is_exec_true)

    def test_check_help(self):
        """
        Function that verifies that each command give a result
        """
        commands = ["create", "all", "show", "destroy", "update"]
        with patch('sys.stdout', new=StringIO()) as help_val:
            for command in commands:
                HBNBCommand().onecmd(f"help {command}")
                self.assertTrue(len(help_val.getvalue()) > 0)

    def test_create_good(self):
        """
        Function to create   another function with valid arguments.
        """
        with patch('sys.stdout', new=StringIO()) as help_val:
            HBNBCommand().onecmd("create BaseModel")
            self.assertTrue(len(help_val.getvalue()) > 0)

    def test_create_empty(self):
        """
        Function to  create another function with missing class name.
        """
        with patch('sys.stdout', new=StringIO()) as help_val:
            HBNBCommand().onecmd("create")
            self.assertEqual(help_val.getvalue(), "** class name missing **\n")

    def test_create_unknown(self):
        """
        Function to test  the create function with an unknown class name.
        """
        with patch('sys.stdout', new=StringIO()) as val:
            HBNBCommand().onecmd("create Holberton")
            self.assertEqual(val.getvalue(), "** class doesn't exist **\n")

    def test_show(self):
        """ Function to test the  command with valid parameters """
        with patch('sys.stdout', new=StringIO()) as val:
            HBNBCommand().onecmd('create BaseModel')
            basemodel_id = val.getvalue()
            self.assertTrue(len(basemodel_id) > 0)
        with patch('sys.stdout', new=StringIO()) as val:
            HBNBCommand().onecmd(f'show BaseModel {basemodel_id}')
            self.assertTrue(val.getvalue() != "** no instance found **\n")

    def test_show_notfound(self):
        """ Function to test command with a non-existing class """
        with patch('sys.stdout', new=StringIO()) as val:
            HBNBCommand().onecmd('show helloo')
            self.assertTrue(val.getvalue() == "** class doesn't exist **\n")

    def test_show_empty(self):
        """ Function to test commands  with missing class """
        with patch('sys.stdout', new=StringIO()) as val:
            HBNBCommand().onecmd('show')
            self.assertTrue(val.getvalue() == "** class name missing **\n")

    def test_show_id(self):
        """ Function to test the  command with missing identity """
        with patch('sys.stdout', new=StringIO()) as val:
            HBNBCommand().onecmd('show BaseModel')
            self.assertTrue(val.getvalue() == "** instance id missing **\n")

    def test_destroy_empty(self):
        """ Function to test the command 'destroy' with missing class """
        with patch('sys.stdout', new=StringIO()) as val:
            HBNBCommand().onecmd('destroy')
            self.assertTrue(val.getvalue() == "** class name missing **\n")

    def test_destroy_wrong(self):
        """Function to  test the  command 'destroy' with non-existing class name """
        with patch('sys.stdout', new=StringIO()) as val:
            HBNBCommand().onecmd('destroy fakeclass')
            self.assertTrue(val.getvalue() == "** class doesn't exist **\n")

    def test_destroy_id(self):
        """ Function to test the command "destroy" with missing ID """
        with patch('sys.stdout', new=StringIO()) as val:
            HBNBCommand().onecmd('destroy BaseModel')
            self.assertTrue(val.getvalue() == "** instance id missing **\n")

    def test_destroy_notfound(self):
        """Function to test the  command "destroy" without an idID """
        with patch('sys.stdout', new=StringIO()) as val:
            HBNBCommand().onecmd('create BaseModel')
        with patch('sys.stdout', new=StringIO()) as val:
            HBNBCommand().onecmd('destroy BaseModel 121212')
            self.assertTrue(val.getvalue() == "** no instance found **\n")

    def test_destroy_working(self):
        """ Function to test the command "destroy" with a valid instance """
        with patch('sys.stdout', new=StringIO()) as val:
            HBNBCommand().onecmd('create BaseModel')
            basemodel_id = val.getvalue()
            self.assertTrue(len(basemodel_id) > 0)
        with patch('sys.stdout', new=StringIO()) as val:
            HBNBCommand().onecmd(f'destroy BaseModel {basemodel_id}')
            self.assertTrue(val.getvalue() != "** no instance found **\n")

    def test_all_fakeclass(self):
        """ Function that test the all command without classes """
        with patch('sys.stdout', new=StringIO()) as val:
            HBNBCommand().onecmd('create BaseModel')
        with patch('sys.stdout', new=StringIO()) as val:
            HBNBCommand().onecmd('all FakeClass')
            self.assertTrue(val.getvalue() == "** class doesn't exist **\n")

    def test_all_working(self):
        """ Function to test the all command with  instances """
        with patch('sys.stdout', new=StringIO()) as val:
            HBNBCommand().onecmd('create BaseModel')
        with patch('sys.stdout', new=StringIO()) as val:
            HBNBCommand().onecmd('all')
            self.assertTrue(len(val.getvalue()) > 0)

    def test_all_trueclass(self):
        """ Function to test the all command with a valid class """
        with patch('sys.stdout', new=StringIO()) as val:
            HBNBCommand().onecmd('create BaseModel')
        with patch('sys.stdout', new=StringIO()) as val:
            HBNBCommand().onecmd('all BaseModel')
            self.assertTrue(len(val.getvalue()) > 0)

    def test_update_missingclass(self):
        """ Function to test the command "command" without class """
        with patch('sys.stdout', new=StringIO()) as val:
            HBNBCommand().onecmd('update')
            self.assertTrue(val.getvalue() == "** class name missing **\n")

    def test_update_wrongclass(self):
        """ Function to test  the update command with non-existing class """
        with patch('sys.stdout', new=StringIO()) as val:
            HBNBCommand().onecmd('create BaseModel')
        with patch('sys.stdout', new=StringIO()) as val:
            HBNBCommand().onecmd('update FakeClass')
            self.assertTrue(val.getvalue() == "** class doesn't exist **\n")

    def test_update_noinstance(self):
        """ Function to add command with missing instance ID """
        with patch('sys.stdout', new=StringIO()) as val:
            HBNBCommand().onecmd('create BaseModel')
        with patch('sys.stdout', new=StringIO()) as val:
            HBNBCommand().onecmd('update BaseModel')
            self.assertTrue(val.getvalue() == "** instance id missing **\n")

    def test_update_notfound(self):
        """ Function to add command  with non-existing instance ID """
        with patch('sys.stdout', new=StringIO()) as val:
            HBNBCommand().onecmd('create BaseModel')
        with patch('sys.stdout', new=StringIO()) as val:
            HBNBCommand().onecmd('update BaseModel 121212')
            self.assertTrue(val.getvalue() == "** no instance found **\n")

    def test_update_missing_name(self):
        """Function to  the update command without the name of attributes"""
        with patch('sys.stdout', new=StringIO()) as my_id:
            HBNBCommand().onecmd('create BaseModel')
            basemodel_id = my_id.getvalue()
            self.assertTrue(len(basemodel_id) > 0)
        with patch('sys.stdout', new=StringIO()) as val:
            HBNBCommand().onecmd(f'update BaseModel {basemodel_id}')
            self.assertTrue(val.getvalue() == "** attribute name missing **\n")

    def test_update_missing_value(self):
        """ Function to test the  update command without attribute value """
        with patch('sys.stdout', new=StringIO()) as my_id:
            HBNBCommand().onecmd('create BaseModel')
            base_id = my_id.getvalue()
            self.assertTrue(len(base_id) > 0)
        with patch('sys.stdout', new=StringIO()) as val:
            HBNBCommand().onecmd(f'update BaseModel {base_id} first_name')
            self.assertTrue(val.getvalue() == "** value missing **\n")

    def test_update_ok(self):
        """ Function that test the update command with valid parameters """
        with patch('sys.stdout', new=StringIO()) as val:
            HBNBCommand().onecmd


class TestConsoleClass(unittest.TestCase):
    """This is a unittest for the console commands related to various classes."""

    def setUp(self):
        """Function to set up the environment for performing test."""
        with open("test.json", 'w'):
            FileStorage._FileStorage__file_path = "test.json"
            FileStorage._FileStorage__objects = {}

    def tearDown(self):
        """Function to eraese after testing."""
        FileStorage._FileStorage__file_path = "file.json"
        try:
            os.remove("test.json")
        except FileNotFoundError:
            pass

    def _test_console_class(self, class_name):
        """Function that test console commands for a specific class.

        """
        with patch('sys.stdout', new=StringIO()) as val:
            HBNBCommand().onecmd(f"create {class_name}")
            instance_id = val.getvalue()
            self.assertTrue(instance_id != f"** class doesn't exist **\n")

        with patch('sys.stdout', new=StringIO()) as val:
            HBNBCommand().onecmd(f"show {class_name} {instance_id}")
            self.assertTrue(val.getvalue() != "** no instance found **\n")

        with patch('sys.stdout', new=StringIO()) as val:
            HBNBCommand().onecmd(f"all {class_name}")
            self.assertTrue(val.getvalue() != "** class doesn't exist **\n")

        with patch('sys.stdout', new=StringIO()) as val:
            HBNBCommand().onecmd(
                    f"update {class_name} {instance_id} name betty"
                    )
            HBNBCommand().onecmd(f"show {class_name} {instance_id}")
            self.assertTrue("betty" in val.getvalue())

        with patch('sys.stdout', new=StringIO()) as val:
            HBNBCommand().onecmd(f"destroy {class_name} {instance_id}")

        with patch('sys.stdout', new=StringIO()) as val:
            HBNBCommand().onecmd(f"show {class_name} {instance_id}")
            self.assertEqual(val.getvalue(), "** no instance found **\n")

    def test_place_console(self):
        """Function to test console commands for the Place class."""
        self._test_console_class("Place")

    def test_state_console(self):
        """Function to test console commands for the State class."""
        self._test_console_class("State")

    def test_city_console(self):
        """Function to test all console commands for the City class."""
        self._test_console_class("City")

    def test_amenity_console(self):
        """Function to test all console commands for the Amenity class."""
        self._test_console_class("Amenity")

    def test_review_console(self):
        """Function to test console commands for the Review class."""
        self._test_console_class("Review")

    def test_alternative_all(self):
        """Function to test alternativeway of using all command with [class].all."""
        with patch('sys.stdout', new=StringIO()) as val:
            HBNBCommand().onecmd("create User")
        with patch('sys.stdout', new=StringIO()) as val:
            HBNBCommand().onecmd("User.all()")
            self.assertTrue(len(val.getvalue()) > 0)

    def test_alternative_show(self):
        """Function to test the alternative way to execute show command with [class].show."""
        with patch('sys.stdout', new=StringIO()) as val:
            HBNBCommand().onecmd("create User")
            user_id = val.getvalue()
        with patch('sys.stdout', new=StringIO()) as val:
            HBNBCommand().onecmd(f"User.show(\"{user_id}\")")
            self.assertTrue(len(val.getvalue()) > 0)

    def test_count(self):
        """Function that test alternativecommand of using show with [class].show."""
        with patch('sys.stdout', new=StringIO()) as val:
            HBNBCommand().onecmd("User.count()")
            self.assertTrue(int(val.getvalue()) == 0)
        with patch('sys.stdout', new=StringIO()) as val:
            HBNBCommand().onecmd("create User")
        with patch('sys.stdout', new=StringIO()) as val:
            HBNBCommand().onecmd("User.count()")
            self.assertTrue(int(val.getvalue()) == 1)

    def test_alternative_destroy(self):
        """Function to test the alternativeof using  destroy command with [class].destroy(id)."""
        with patch('sys.stdout', new=StringIO()) as val:
            HBNBCommand().onecmd("create User")
            user_id = val.getvalue()
        with patch('sys.stdout', new=StringIO()) as val:
            HBNBCommand().onecmd(f"User.destroy(\"{user_id}\")")
        with patch('sys.stdout', new=StringIO()) as val:
            HBNBCommand().onecmd("User.count()")
            self.assertTrue(int(val.getvalue()) == 0)

    def test_alternative_update(self):
        """Function to test alternative update using [class].show."""
        with patch('sys.stdout', new=StringIO()) as val:
            HBNBCommand().onecmd("create User")
            user_id = val.getvalue()
        with patch('sys.stdout', new=StringIO()) as val:
            line = "\", \"name\", \"betty\")"
            HBNBCommand().onecmd(f"User.update(\"{user_id}{line}")
        with patch('sys.stdout', new=StringIO()) as val:
            HBNBCommand().onecmd(f"User.show(\"{user_id}\")")
            self.assertTrue("betty" in val.getvalue())

    if __name__ == '__main__':
        unittest.main()
