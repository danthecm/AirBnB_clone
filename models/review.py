#!/usr/bin/python3
"""
User module for User Model inheriting from BaseModel
"""

from models.base_model import BaseModel


class Review(BaseModel):
    place_id = ""
    user_id = ""
    text = ""
