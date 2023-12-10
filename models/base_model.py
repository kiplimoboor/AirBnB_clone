#!/usr/bin/python3
"""
This module defines a class Basemodel that defines all common attributes
 and methods from other classes
"""

import models
import uuid
from datetime import datetime


class BaseModel:
    """
    This is the base model of the airbnb clone project.
    """

    def __init__(self, *args, **kwargs):
        """
        Initializes the BaseModel
        """
        if kwargs:
            for key, value in kwargs.items():
                if key != '__class__':
                    if key in ["created_at", "updated_at"]:
                        setattr(self, str(key), datetime.fromisoformat(value))
                    else:
                        setattr(self, str(key), value)
        else:
            self.id = str(uuid.uuid4())
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
        """
        Saves the model
        """

        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """Finds dictionary representaion of mode

        Returns:
            dict: the doctionary respresentation of the model
        """
        dictionary = self.__dict__.copy()
        dictionary['__class__'] = self.__class__.__name__
        dictionary['created_at'] = self.created_at.isoformat()
        dictionary['updated_at'] = self.updated_at.isoformat()

        return dictionary
