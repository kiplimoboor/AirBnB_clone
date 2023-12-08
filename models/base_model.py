#!/usr/bin/python3
"""
This module defines a class Basemodel that defines all common attributes
 and methods from other classes
"""


import uuid
from datetime import datetime
from models import storage


class BaseModel:
    """
    This is the base class...more details to be added later
    """

    def __init__(self, *args, **kwargs):

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
        storage.save()

    def to_dict(self):
        """
        Returns a dictionary containing all keys/values of the instance
        """
        dictionary = self.__dict__.copy()
        dictionary['__class__'] = self.__class__.__name__
        dictionary['created_at'] = datetime.isoformat(self.created_at)
        dictionary['updated_at'] = datetime.isoformat(self.updated_at)

        return dictionary
