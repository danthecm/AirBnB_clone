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

    def __init__(self, *args, **kwargs):
        """
        Initialization method for the base model class
        """
        if len(kwargs):
            for key, value in kwargs.items():
                if key == "__class__":
                    continue
                elif key == "created_at" or key == "updated_at":
                    value = datetime.fromisoformat(value)
                setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()

    def __str__(self):
        """
        String representation of the base model class
        """
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
        dict_rep["created_at"] = str(self.created_at.isoformat())
        dict_rep["updated_at"] = str(self.updated_at.isoformat())
        return dict_rep
