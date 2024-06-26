#!/usr/bin/python3
"""This module is used to unittest different methods and attributes"""
import unittest
import uuid
from datetime import datetime
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """This class inherits the TestCase class and
    is a wrapper for testing methods"""
    def setUp(self):
        """The method is used to arrange for test cases"""
        self.bs = BaseModel()
        self.obj = BaseModel(id="123")

    def test_public_instance_id(self):
        """This method tests the different requirement for the id attribute"""
        self.assertTrue(self.bs.id)
        self.assertIsInstance(self.bs.id, str)
        self.assertTrue(uuid.UUID(self.bs.id).version == 4)

    def test_public_instance_created_at(self):
        """This method tests the different requirement for
        the created_at attribute"""
        self.assertTrue(self.bs.created_at)
        self.assertIsInstance(self.bs.created_at, datetime)

    def test_public_instance_updated_at(self):
        """This method tests the different requirement
        for the updated_at attribute"""
        self.assertTrue(self.bs.updated_at)
        self.assertIsInstance(self.bs.updated_at, datetime)

    def test_public_insMethod_save(self):
        """This method test the save method"""
        self.assertTrue(self.bs.save)
        self.bs.save()
        prevUpdatedTime = self.bs.updated_at
        now = datetime.now()
        self.assertNotEqual(prevUpdatedTime, now)

    def test_public_insMethod_to_dict(self):
        """This method tests the requirements for the to_dict method"""
        mydict = self.bs.to_dict()
        self.assertTrue(mydict["__class__"])
        crt = mydict["created_at"]
        upt = mydict["updated_at"]
        originalcrt = datetime.isoformat(self.bs.__dict__["created_at"])
        originalupt = datetime.isoformat(self.bs.__dict__["updated_at"])
        self.assertEqual(crt, originalcrt)
        self.assertEqual(upt, originalupt)

    def test_public_insMethod__str__(self):
        """This method test the string rep of the object"""
        returned_str = self.obj.__str__()
        expected = "[BaseModel] (123) {'id': '123'}"
        self.assertEqual(returned_str, expected)


if __name__ == "__main__":
    unittest.main()
