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
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """
        Saves all changes made to the model and updates
        the updated_at timestamp
        """
        self.updated_at = datetime.now()

    def to_dict(self):
        """
        Returns a dictionary representation of the model
        including the class name as __class__ and isoformat
        of the created_at and updated_at
        """
        dict_rep = {**self.__dict__}
        dict_rep["__class__"] = self.__class__.__name__
        dict_rep["created_at"] = self.created_at.isoformat()
        dict_rep["updated_at"] = self.updated_at.isoformat()
        return dict_rep
