#!/usr/bin/python3
"""
This module defines a class FileStorage that serializes instances
to a JSON file and deserializes JSON file to instances
Args:
  Private Class Attributes
  Public Instance Method
"""
import json
from models.base_model import BaseModel
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User


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
        return FileStorage.__objects

    def new(self, obj):
        """
        sets in __objects the obj with key <obj class name>.id
        """
        key = f"{type(obj).__name__}.{obj.id}"
        FileStorage.__objects[key] = obj

    def save(self):
        """
        serializes __objects to the JSON file (path: __file_path)
        """
        serialized_objects = {}
        for key, obj in FileStorage.__objects.items():
            serialized_objects[key]

        with open(FileStorage.__filepath, 'w') as json_file:
            json.dump(serialized_objects, file)

    def reload(self):
        """
        deserializes the JSON file to __objects
        """
        filename = FileStorage.__file_path

        try:
            with open(filename, 'r') as json_file:
                models_data = json.load(json_file)
                for key, value in models_data.items():
                    class_name, obj_id = key.split('.')
                    class_obj = eval(class_name)
                        instance = class_obj(**value)
                        FileStorage.__objects[key] = instance
        except FileNotFoundError:
            pass
        except json.JSONDecodeError:
            pass
