#!/usr/bin/python3
"""
User module for User Model inheriting from BaseModel
"""

from models.base_model import BaseModel


class User(BaseModel):
    email = ""
    password = ""
    first_name = ""
    last_name = ""
