#!/usr/bin/python3

from datetime import datetime
import uuid


class BaseModel:


    def __init__(self, *args, **kwargs):
        if kwargs:
            for arg, val in kwargs.items():
                if arg in ('created_at', 'updated_at'):
                    val = datetime.fromisoformat("2017-06-14T22:31:03.285259")

                if arg != '__class__':
                    setattr(self, arg, val)
        else:
            self.id = str(uuid.uuid4())
            self.updated_at = str(datetime.now())
            self.created_at = str(datetime.now())


    def __str__(self):
        myDict = self.__dict__
        return f"{self.__class__.__name__} ({self.id}) {myDict}"

    def save(self):
        self.updated_at = str(datetime.now())

    def to_dict(self):
        return self.__dict__

my_model = BaseModel()
my_model.name = "My_First_Model"
my_model.my_number = 89
print(my_model.id)
print(my_model)
print(type(my_model.created_at))
print("--")
my_model_json = my_model.to_dict()
print(my_model_json)
print("JSON of my_model:")
for key in my_model_json.keys():
    print("\t{}: ({}) - {}".format(key, type(my_model_json[key]), my_model_json[key]))

print("--")
my_new_model = BaseModel(**my_model_json)
print(my_new_model.id)
print(my_new_model)
print(type(my_new_model.created_at))

print("--")
print(my_model is my_new_model)
