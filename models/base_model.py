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

    Properties:
        *args: not used
        **kwargs: key/value pairs of attributes
    """

    def __init__(self, *args, **kwargs):
        """Initializes a new BaseModel"""

        time_format = "%Y-%m-%dT%H:%M:%S.%f"
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
        if len(kwargs) != 0:
            for key, value in kwargs.items():
                if key in ["created_at", "updated_at"]:
                        setattr(self, str(key), datetime.strptime(value, time_format))
                else:
                        setattr(self, str(key), value)
        else:
            storage.new(self.to_dict())

    def __str__(self):
        """
        Returns the string representation of the instance
        """

        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """
        Updates the public instance attribute updated_at with current datetime
        """

        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """
        Returns a dictionary containing all keys/values of the instance
        """
        dictionary = self.__dict__.copy()
        dictionary['__class__'] = self.__class__.__name__
        dictionary['created_at'] = self.created_at.isoformat()
        dictionary['updated_at'] = self.updated_at.isoformat()

        return dictionary
