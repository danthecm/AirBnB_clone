#!/usr/bin/python3
"""
User module for User Model inheriting from BaseModel
"""

from models.base_model import BaseModel


class City(BaseModel):
    state_id = ""
    name = ""
