#!/usr/bin/python3
"""This module defines the BaseModel class,
which is the base class of all other classes"""

import uuid
from datetime import datetime


class BaseModel():
    """This is the BaseModel class definition"""
    def __init__(self, *args, **kwargs):
        """The __init___ method acts as a constructor"""
        if kwargs:
            for key, value in kwargs.items():
                if key in ['__class__']:
                    continue
                if key in ['created_at', 'updated_at']:
                    dt = datetime.strptime(value, '%Y-%m-%dT%H:%M:%S')
                    self.__dict__[key] = dt
                else:
                    self.__dict__[key] = value
        else:
            uid = uuid.uuid4()
            self.id = str(uid)
            self.created_at = datetime.now().replace(microsecond=0)
            self.updated_at = datetime.now().replace(microsecond=0)
            from models import storage
            storage.new(self)

    def save(self):
        """The save method is used to save the updated time of the object"""
        self.updated_at = datetime.now().replace(microsecond=0)
        from models import storage
        storage.save()

    def to_dict(self):
        """The to_dict method returns a dictionary with some changes
        to the orignal __dict__"""
        mydict = self.__dict__.copy()
        mydict["__class__"] = self.__class__.__name__
        crt = datetime.isoformat(mydict["created_at"])
        upt = datetime.isoformat(mydict["updated_at"])
        mydict["created_at"] = crt
        mydict["updated_at"] = upt
        return mydict

    def __str__(self):
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"
