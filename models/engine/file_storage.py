#!/usr/bin/python3
"""
File storage module containing a FileStorage class
"""
import json
from datetime import datetime


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
        return self.__objects

    def new(self, obj):
        """
        Addes a new object to the object of saved objects
        Args:
        obj: the object to be saved
        """
        self.__objects[f"{obj.__class__.__name__}.{obj.id}"] = obj

    def save(self):
        """
        Serializes the object to a json file
        """
        with open(self.__file_path, "w") as f:
            new_obj = {}
            for key, value in self.__objects.items():
                # print(f"About to save: {value}")
                dict_val = value.to_dict()
                new_obj[key] = dict_val
            f.write(json.dumps(new_obj))

    def reload(self, object):
        """
        Deserializes the object from the json file
        """
        try:
            with open(self.__file_path, "r") as f:
                self.__objects = json.loads(f.read())
                for key, value in self.__objects.items():
                    self.__objects[key] = object(**value)
                # print(f"Reloaded objects {self.__objects}")
        except Exception as e:
            # print(f"Error reloading objects {e}")
            pass
