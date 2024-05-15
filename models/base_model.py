#!/usr/bin/python3
"""This module defines the BaseModel class,
which is the base class of all other classes"""

import uuid
from datetime import datetime


class BaseModel():
    """This is the BaseModel class definition"""
    def __init__(self):
        """The __init___ method acts as a constructor"""
        uid = uuid.uuid4()
        self.id = str(uid)
        self.created_at = datetime.now().replace(microsecond=0)
        self.updated_at = datetime.now().replace(microsecond=0)

    def save(self):
        """The save method is used to save the updated time of the object"""
        self.updated_at = datetime.now().replace(microsecond=0)

    def to_dict(self):
        """The to_dict method returns a dictionary with some changes
        to the orignal __dict__"""
        self.mydict = self.__dict__.copy()
        self.mydict["__class__"] = self.__class__.__name__
        crt = datetime.isoformat(self.mydict["created_at"])
        upt = datetime.isoformat(self.mydict["updated_at"])
        self.mydict["created_at"] = crt
        self.mydict["updated_at"] = upt
        return self.mydict

    def __str__(self):
        return f"[{self.__class__.__name__}] {(self.id)} {self.__dict__}"
