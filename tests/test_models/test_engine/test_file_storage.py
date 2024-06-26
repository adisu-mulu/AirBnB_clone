#!/usr/bin/python3
"""This module defines the unittest for FileStorage"""
import unittest
import json
import os
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel


class TestFileStorage(unittest.TestCase):
    """Defines the Test class by inheriting unittest"""
    def setUp(self):
        """Initializes the classes with instances"""
        self.fs = FileStorage()
        self.base_model = BaseModel()

    def test_private_class_attributes(self):
        """Provides test cases for all class attributes"""
        self.assertTrue(hasattr(FileStorage, '_FileStorage__file_path'))
        self.assertTrue(hasattr(FileStorage, '_FileStorage__objects'))

    def test_check_prAttributes_type(self):
        """Provides test cases for the types of attributes"""
        self.assertIsInstance(self.fs._FileStorage__file_path, str)
        self.assertIsInstance(self.fs._FileStorage__objects, dict)

    def test_public_instance_method_all(self):
        """provides test case for the all method"""
        self.assertTrue(hasattr(self.fs, 'all'))
        self.objs = self.fs.all()
        self.assertIs(self.objs, self.fs._FileStorage__objects)

    def test_public_instance_method_new(self):
        """provides test cases for the new method"""
        self.assertTrue(hasattr(self.fs, 'new'))
        self.fs.new(self.base_model)
        myobj = self.base_model.__class__.__name__ + '.' + self.base_model.id
        self.assertIn(myobj, self.fs._FileStorage__objects)

    def test_public_instance_method_save(self):
        """Provides test cases for the save method"""
        self.assertTrue(hasattr(self.fs, 'save'))
        jsonString = json.dumps(self.fs._FileStorage__objects)
        self.fs.save()
        with open('file.json') as file:
            jfile = file.read()
            self.assertIsInstance(jsonString, BaseModel)

    def test_public_instance_method_reload(self):
        """Provides the test cases for the reload method"""
        self.assertTrue(hasattr(self.fs, 'reload'))
        fp = self.fs._FileStorage__file_path
        if os.path.exists(fp):
            with open(fp, 'r') as file:
                myobj = json.load(file)
                self.fs._FileStorage__objects = myobj
                self.assertEqual(myobj, self.fs._FileStorage__objects)
