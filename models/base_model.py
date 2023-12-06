#!/usr/bin/python3
"""
This module defines a class Basemodel that defines all common attributes
 and methods from other classes
"""


import uuid
from datetime import datetime


class BaseModel:
    """
    This is the base class...more details to be added later
    """

    def __init__(self):
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def updated_time(self):
        self.updated_at = datetime.now()
    
    def __str__(self):
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"
