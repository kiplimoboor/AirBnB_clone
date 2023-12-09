#!/usr/bin/python3
"""
This module defines a class FileStorage that serializes instances
to a JSON file and deserializes JSON file to instances
"""

import json


class FileStorage:
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
        key = f"{obj['__class__']}.{obj['id']}"
        self.__objects[key] = obj

    def save(self):
        """
        serializes __objects to the JSON file (path: __file_path)
        """
        filename = self.__file_path
        with open(filename, 'w') as json_file:
            json.dump(self.__objects, json_file)

    def reload(self):
        """
        deserializes the JSON file to __objects
        """
        try:
            filename = self.__file_path
            with open(filename, 'r') as json_file:
                self.__objects = json.load(json_file)
        except FileNotFoundError:
            pass
