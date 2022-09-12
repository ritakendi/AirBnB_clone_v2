#!/usr/bin/python3
"""amenity unittest module"""

import unittest
import os
from models.engine.file_storage import FileStorage
from models.amenity import Amenity


class TestAmenity(unittest.TestCase):
    """test csae for amenity"""

    def test_docstring(self):
        """ checks if docstring is there """
        self.assertIsNotNone(Amenity.__doc__)

    def test_amenity(self):
        """ checks amenity """
        a = Amenity()
        self.assertEqual(type(a), Amenity)
        self.assertEqual(a.name, "")
        a.name = "b"
        self.assertEqual(a.name, "b")

    def test_save_is_dict(self):
        """ tests to see if the return type of save is a string """
        bm = Amenity()
        bm.save()
        self.assertIsInstance(bm.to_dict()['created_at'], str)
        self.assertIsInstance(bm.to_dict()['updated_at'], str)

    def test_has_attr(self):
        """ tests if the base model has the attr """
        self.assertTrue(hasattr(Amenity, "save"))


if __name__ == "__main__":
    unittest.main()
