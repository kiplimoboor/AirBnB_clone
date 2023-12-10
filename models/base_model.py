#!/usr/bin/python3
"""
Defines the Basemodel class with common attributes and
methods from other classes

@Attributes:
  id: assings a unique uuid to id
  created_at: assigns the current datetime when an instance is created
  updated_at: assigns the current datetime every time an instance is updated

@Methods:
  def save: updates the public instance attribute updated_at
  def to_dict: returns a dictionaary containing keys/values of __dict__
"""
import models
from uuid import uuid4
from datetime import datetime


class BaseModel:
    """
    This is the base model of the airbnb clone project.
    @properties:
      __init__: initializes the class
      __str__: returns a formatted string
      to_dict: returns the dictionary representation of model
    """

    def __init__(self, *args, **kwargs):
        """
        Initializes the BaseModel
        """
        if kwargs:
            for key, value in kwargs.items():
                if key == '__class__':
                    continue
                elif key in ["created_at", "updated_at"]:
                    setattr(self, str(key), datetime.fromisoformat(value))
                else:
                    setattr(self, str(key), value)
        else:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

    def __str__(self):
        """
        Creates string representation of BaseModel

        Returns:
            string: the formatted string representation
        """

        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """Saves the model"""
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """Finds dictionary representaion of mode

        Returns:
            dict: the dictionary respresentation of the model
        """
        dictionary = self.__dict__.copy()
        dictionary['__class__'] = self.__class__.__name__
        dictionary['created_at'] = self.created_at.isoformat()
        dictionary['updated_at'] = self.updated_at.isoformat()

        return dictionary
