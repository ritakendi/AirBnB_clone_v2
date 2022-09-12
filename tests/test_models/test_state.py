#!/usr/bin/python3
"""State unittest module"""

import unittest
import os
from models.state import State
from models.engine.file_storage import FileStorage


class TestState(unittest.TestCase):
    """test case for State"""

    def test_docstring(self):
        """ checks if docstring is there """
        self.assertIsNotNone(State.__doc__)

    def test_state(self):
        """ testing state class """
        s = State()
        self.assertEqual(type(s), State)
        self.assertEqual(s.name, "")
        s.name = "CA"
        self.assertEqual(s.name, "CA")

    def test_save_is_dict(self):
        """ tests to see if the return type of save is a string """
        bm = State()
        bm.save()
        self.assertIsInstance(bm.to_dict()['created_at'], str)
        self.assertIsInstance(bm.to_dict()['updated_at'], str)

    def test_has_attr(self):
        """ tests if the base model has the attr """
        self.assertTrue(hasattr(State, "save"))


if __name__ == "__main__":
    unittest.main()
