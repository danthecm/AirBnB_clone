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
        my_objects = {}
        for key, value in self.__objects.items():
            for obj_key, obj_value in value.items():
                if obj_key == "created_at" or obj_key == "updated_at":
                    value[obj_key] = datetime.fromisoformat(
                        obj_value)
            my_objects[key] = value
        return my_objects

    def new(self, obj):
        """
        Addes a new object to the object of saved objects
        Args:
        obj: the object to be saved
        """
        self.__objects[f"{obj.__class__.__name__}.{obj.id}"] = obj.__dict__

    def save(self):
        """
        Serializes the object to a json file
        """
        with open(self.__file_path, "w") as f:
            new_obj = {}
            for key, value in self.__objects.items():
                for obj_key in value.keys():
                    if obj_key == "created_at" or obj_key == "updated_at":
                        value[obj_key] = value[obj_key].isoformat()
                new_obj[key] = value
            f.write(json.dumps(new_obj))

    def reload(self):
        """
        Deserializes the object from the json file
        """
        try:
            with open(self.__file_path, "r") as f:
                self.__objects = json.loads(f.read())
        except Exception as e:
            pass
