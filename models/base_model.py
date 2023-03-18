#!/usr/bin/python3
from datetime import datetime
import uuid
"""
This Module contains a base model class 
"""


class BaseModel:
    """
    A base class for all models containng necessary methods
    to create, update and manipulate models
    """

    def __init__(self):
        self.id = uuid.uuid4()
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"


my_base = BaseModel()
# print(my_base.id, my_base.created_at, my_base.updated_at)
print(my_base)
