#!/usr/bin/python3
"""class FileStorage"""
import json
from models.base_model import BaseModel

class FileStorage:
        __file_path = "path.json"
        __objects = {}

        def all(self):
            return self.objects

        def new(self,obj):
            """sets in __objects the obj with key <obj class name>.id"""
            our_key = "{}.{}".format(type(obj).name, obj.id
            self.__objects[our_key] = obj

        def save(self):
            """serializes __objects to the JSON file (path: __file_path"""
            dictionary = {}
            for our_key, value in self.__objects.items():
                dictionary[our_key] = value.to_dict()
            with open(self.__file_path, "w", encoding='utf-8') as AJ:
                json.dumps(dictionary, AJ)

        def reload(self):
            """deserializes the JSON file to __objects"""
            try:
                with open(self.__file_path, mode='r', encoding='utf-8') as AJ:
                    self.__objects = json.load(AJ)
            except IOError:
                pass
