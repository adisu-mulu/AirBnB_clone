#!/usr/bin/python3
"""This module is used to unittest different methods and attributes"""
import unittest
import uuid
from datetime import datetime
from models.place import Place


class TestPlace(unittest.TestCase):
    """This class inherits the TestCase class and
    is a wrapper for testing methods"""
    def setUp(self):
        """The method is used to arrange for test cases"""
        self.user = Place()

    def test_public_instances(self):
        """This method tests the different requirement for the id attribute"""
        self.assertEqual(Place().city_id, "")
        self.assertEqual(Place().user_id, "")
        self.assertEqual(Place().name, "")
        self.assertEqual(Place().description, "")
        self.assertEqual(Place().number_rooms, 0)
        self.assertEqual(Place().number_bathrooms, 0)
        self.assertEqual(Place().max_guest, 0)
        self.assertEqual(Place().price_by_night, 0)
        self.assertEqual(Place().latitude, 0.0)
        self.assertEqual(Place().longitude, 0.0)
        self.assertEqual(Place().amenity_ids, [])
