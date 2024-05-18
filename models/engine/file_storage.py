#!/usr/bin/python3
"""This module defines the storage system for the appln"""
import json
import os
from models.base_model import BaseModel


class FileStorage():
    """The class defines and wraps the methods and class attributes"""
    __file_path = 'file.json'
    __objects = {}

    def all(self):
        """This method returns all the objects"""
        return self.__objects

    def new(self, obj):
        """This method updates objects dict with new instances"""
        self.cls_name = obj.__class__.__name__
        self.obj_id = obj.id
        self.obj_full = self.cls_name + '.' + self.obj_id
        self. __objects.update({self.obj_full: obj})

    def save(self):
        """Saves the objects dict to file"""
        with open(self.__file_path, 'w') as file:
            json.dump({k: v.to_dict() for k, v in self.__objects.items()},
                      file)

    def reload(self):
        """Reloads all objects from file on startup"""
        if os.path.exists(self.__file_path):
            with open(self.__file_path, 'r') as file:
                objects_in_file = json.load(file)
                for key, value in objects_in_file.items():
                    self.__objects[key] = BaseModel(**value)
