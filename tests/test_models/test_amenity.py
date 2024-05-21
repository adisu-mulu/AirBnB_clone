#!/usr/bin/python3
"""This module is used to unittest different methods and attributes"""
import unittest
import uuid
from datetime import datetime
from models.amenity import Amenity


class TestAmenity(unittest.TestCase):
    """This class inherits the TestCase class and
    is a wrapper for testing methods"""
    def setUp(self):
        """The method is used to arrange for test cases"""
        self.user = Amenity()

    def test_public_instances(self):
        """This method tests the different requirement for the id attribute"""
        self.assertEqual(Amenity().name, "")

