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
        key = str(str(obj.__class__.__name__) + "." + obj.id)
        self.__objects[key] = obj.to_dict()

    def save(self):
        filename = self.__file_path
        with open(filename, 'w') as json_file:
            json.dump(self.__objects, json_file)

    def reload(self):
        try:
            filename = self.__file_path
            with open(filename, 'r') as json_file:
                self.__objects = json.load(json_file)
        except FileNotFoundError:
            pass
