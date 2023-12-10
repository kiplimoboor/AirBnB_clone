#!/usr/bin/python3
"""
This module defines a class User that inherits from BaseModel
"""


from models.base_model import BaseModel


class User(BaseModel):
    """
    This class updates file storage and console.
    @properties:
        email: empty string
        password: empty string
        first_name: empty string
        last_name: empty string
    """

    email = ""
    password = ""
    first_name = ""
    last_name = ""
