#!/usr/bin/python3
"""
This module defines a class FileStorage that serializes instances
to a JSON file and deserializes JSON file to instances
"""
import json
import uuid
import os
from models.base_model import BaseModel
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User
from datetime import datetime


class FileStorage:
    """
    This class defines a filestorage for all the files in the
    hbnb project
    @Attributes
      __file_path: path to the json file
      __objects: empty but will store all objects

    @Methods:
      def all: returns the dictionary __objects
      def new: sets in __objects the obj with key
      def save: serializes __objects to the json file
      def reload: deserializes the json file to __objects
    """

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """
        Returns the dictionary __objects
        """
        return self.__objects

    def new(self, obj):
        """
        sets in __objects the obj with key <obj class name>.id
        """
        key = f"{type(obj).__name__}.{obj.id}"
        self.__objects[key] = obj

    def save(self):
        """
        serializes __objects to the JSON file (path: __file_path)
        """
        filename = self.__file_path
        with open(filename, 'w') as json_file:
            json.dump({key: value.to_dict()
                       for key, value in self.__objects.items()}, json_file)

    def reload(self):
        """
        deserializes the JSON file to __objects
        """
        classes = {'Amenity': Amenity, 'BaseModel': BaseModel, 'City': City,
                   'Place': Place, 'Review': Review, 'State': State,
                   'User': User}
        filename = self.__file_path

        try:
            with open(filename, 'r') as json_file:
                models = json.load(json_file)
                self.__objects = {key: classes[key.split('.')[0]](**value)
                                  for key, value in models.items()}
        except FileNotFoundError:
            pass
        except json.JSONDecodeError:
            pass
