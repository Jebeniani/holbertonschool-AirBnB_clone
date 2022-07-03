#!/usr/bin/python3
"""a class named BaseModel"""

from datetime import datetime
from uuid import uuid4
import models


class BaseModel:
    """a class named BaseModel"""

    def __init__(self, *args, **kwargs):
        """__init__ method for BaseModel"""
        if kwargs:
            for arg, val in kwargs.items():
                if arg in ('created_at', 'updated_at'):
                    val = datetime.fromisoformat("%Y-%m-%dT%H:%M:%S.%f")

                if arg != '__class__':
                    setattr(self, arg, val)
        else:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = self.created_at
            models.storage.new(self)

    def __str__(self):
        """the class reprresentation to the user"""
        return "[{}] ({}) {}".format(
                self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        """updates the public instance attribute
        updated_at with the current datetime"""
        self.updated_at = datetime.now()
        models.storage.save()


    def to_dict(self):
        """ returns a dictionary containing
        all keys/values of __dict__ of the instance"""
        my_dict = self.__dict__.copy()
        my_dict['__class__'] = self.__class__.__name__
        my_dict['created_at'] = self.created_at.isoformat()
        my_dict['updated_at'] = self.updated_at.isoformat()
        return my_dict
