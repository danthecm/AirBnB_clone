#!/usr/bin/python3
"""
File storage module containing a FileStorage class
"""
import json


class FileStorage():
    """
    FileStorage class for serialization and deserialization
    of models from objects to json and json to objects
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """
        Returns a dictionary of all saved objects
        the key of the dictionaries are the objects name and id
        the value is the object itself
        """
        pass

    def new(self, obj):
        """
        Addes a new object to the object of saved objects
        Args:
        obj: the object to be saved
        """
        pass

    def save(self):
        """
        Serializes the object to a json file
        """
        pass

    def reload(self):
        """
        Deserializes the object from the json file
        """
        pass
