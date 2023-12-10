#!/usr/bin/python3
"""
This module is a magic method __init__ for the
class FileStorage
"""
from models.engine.file_storage import FileStorage


storage = FileStorage()
storage.reload()
