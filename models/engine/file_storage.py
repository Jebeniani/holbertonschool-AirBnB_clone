#!/usr/bin/python3
"""class FileStorage"""
import json
from models.base_model import BaseModel
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models.user import User
from os import path


class FileStorage:
    """File Storage Class"""
    __file_path = "path.json"
    __objects = {}

    def all(self):
        """returns the dictionary __objects"""
        return self.__objects

    def new(self, obj):
        """sets in __objects the obj with key <obj class name>.id"""
        key = obj.__class__.__name__ + '.' + obj.id
        self.__objects[key] = obj

    def save(self):
        """serializes __objects to the JSON file (path: __file_path"""
        dictionary = {}
        for key, value in self.__objects.items():
            dictionary[key] = value.to_dict()
        with open(self.__file_path, "w", encoding='utf-8') as AJ:
            AJ.write(json.dumps(dictionary))

    def reload(self):
        """deserializes the JSON file to __objects"""
        if path.exists(self.__file_path):
            with open(self.__file_path, mode='r', encoding='utf-8') as AJ:
                dictionary = json.loads(AJ.read())
                for key, value in dictionary.items():
                    self.__objects[key] = eval(value['__class__'])(**value)
