#!/usr/bin/python3
"""city unittest module"""

import unittest
import os
from models.engine.file_storage import FileStorage
from models.city import City


class TestCity(unittest.TestCase):
    """test case for City"""

    def test_docstring(self):
        """ checks if docstring is there """
        self.assertIsNotNone(City.__doc__)

    def test_city(self):
        """ checks peter out. whatta hottie """
        c = City()
        self.assertEqual(c.name, "")
        self.assertEqual(c.state_id, "")
        c.name = "San Francisco"
        c.state_id = "98"
        self.assertEqual(c.name, "San Francisco")
        self.assertEqual(c.state_id, "98")
        self.assertEqual(type(c.state_id), str)

    def test_save_is_dict(self):
        """ tests to see if the return type of save is a string """
        bm = City()
        bm.save()
        self.assertIsInstance(bm.to_dict()['created_at'], str)
        self.assertIsInstance(bm.to_dict()['updated_at'], str)

    def test_has_attr(self):
        """ tests if the base model has the attr """
        self.assertTrue(hasattr(City, "save"))


if __name__ == "__main__":
    unittest.main()
