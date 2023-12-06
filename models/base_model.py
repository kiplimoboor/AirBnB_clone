#!/usr/bin/env python3

class BaseModel:
    def __str__(self):
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"