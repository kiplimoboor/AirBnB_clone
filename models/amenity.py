#!/usr/bin/python3
"""
This module defines a class for amenity
"""


from models.base_model import BaseModel


class Amenity(BaseModel):
    """
    An amenity in the app
    @properties:
      name: Name of the amenity
    """
    name = ""
