"""
This module contains tests for the `file_storage` module
"""

import os
import json
import unittest
from models import storage
from models.base_model import BaseModel

filename = "file.json"


class TestFileStorage(unittest.TestCase):
    """
    Test cases for File Storage

    Args:
        unittest (class): unittest class TestCase
    """

    def setUp(self):
        if os.path.exists(filename):
            os.remove(filename)

    def tearDown(self):
        if os.path.exists(filename):
            os.remove(filename)

    def test_all(self):
        b = BaseModel()
        storage.new(b)
        self.assertIn(f"BaseModel.{b.id}", storage.all().keys())

    def test_save(self):
        b = BaseModel()
        b.save()
        self.assertTrue(os.path.exists(filename))

        with open(filename, 'r') as json_file:
            objects = json.load(json_file)
            self.assertIn(f"BaseModel.{b.id}", objects)

    def test_reload(self):
        b1 = BaseModel()
        b1.save()
        storage.reload()

        with open(filename, 'r') as json_file:
            objects = json.load(json_file)
            self.assertIn(f"BaseModel.{b1.id}", objects)

        b2 = BaseModel()
        storage.reload()
        with open(filename, 'r') as json_file:
            objects = json.load(json_file)
            self.assertNotIn(f"BaseModel.{b2.id}", objects)


if __name__ == "__main__":
    unittest.main()
