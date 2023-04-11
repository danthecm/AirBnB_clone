#!/usr/bin/python3
"""
Init file for the models containing base_models.py
"""
import sys
from models.engine import file_storage


storage = file_storage.FileStorage()


if 'base_model' in sys.modules:

    storage.reload(BaseModel)
else:
    from .base_model import BaseModel

    storage.reload(BaseModel)
