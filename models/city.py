#!/usr/bin/python3

"""
Module for city
"""

from models.base_model import BaseModel


class City(BaseModel):
    """
    A city in the app

    Args:
        BaseModel: The parent class
    """
    state_id = ""
    name = ""
