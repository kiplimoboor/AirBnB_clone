"""
This module contains tests for the `file_storage` module
"""

import os
import json
import unittest
import models
from models import storage
from models.base_model import BaseModel

import os
import models
import unittest
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from models.user import User
from models.state import State
from models.place import Place
from models.city import City
from models.amenity import Amenity
from models.review import Review

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
        bm = BaseModel()
        us = User()
        st = State()
        pl = Place()
        cy = City()
        am = Amenity()
        rv = Review()
        models.storage.new(bm)
        models.storage.new(us)
        models.storage.new(st)
        models.storage.new(pl)
        models.storage.new(cy)
        models.storage.new(am)
        models.storage.new(rv)
        models.storage.save()
        models.storage.reload()
        objs = FileStorage._FileStorage__objects
        self.assertIn("BaseModel." + bm.id, objs)
        self.assertIn("User." + us.id, objs)
        self.assertIn("State." + st.id, objs)
        self.assertIn("Place." + pl.id, objs)
        self.assertIn("City." + cy.id, objs)
        self.assertIn("Amenity." + am.id, objs)
        self.assertIn("Review." + rv.id, objs)

    def test_reload_with_arg(self):
        with self.assertRaises(TypeError):
            models.storage.reload(None)


if __name__ == "__main__":
    unittest.main()
