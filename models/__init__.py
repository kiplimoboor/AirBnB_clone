#!/usr/bin/python3
"""
This module packages models
"""


from models.engine.file_storage import FileStorage


storage = FileStorage()
storage.reload()
