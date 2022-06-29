#!/usr/bin/python3
"""class FileStorage"""
from models.base_model import BaseModel

class FileStorage(BaseModel):
    def __init__(self, file_path = None, objects = {}):
        self._file_path = file_path
        self._objects = objects
        super().__init__()

        @property
        def file_path(self):
            return self._file_path

        @file_path.setter
        def file_path(self, value):
            if(type(value) is not str):
                raise ValueError

        @property
        def objects(self):
            return self._objects

        @objects.setter
        def objects(self, value):
            return BaseModel.to_dict()

        def all(self):
            return self.objects

        def new(self,obj):
            #sets in __objects the obj with key <obj class name>.id

        def save(self):
            #serializes __objects to the JSON file (path: __file_path
