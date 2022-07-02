#!/usr/bin/python3
"""class HBNBCommand"""

import cmd
import models
from datetime import datetime
from models.base_model import BaseModel
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models.user import User



class HBNBCommand(cmd.Cmd):
    """cmd processor class"""
    prompt = '(hbnb)'
    our_classes = ['BaseModel']

    def do_EOF(self, line):
        """EOF command to exit the program"""
        return True

    def do_quit(self, line):
        """Quit command to exit the program"""
        return True

    def emptyline(self):
        """emptyLine\n"""
    pass

    def create(self, arg):
        """Creates a new instance of BaseModel"""
        command = self.parseline(line)[0]
        if command is None:
            print("** class name missing **")
        elif command not in self.our_classes:
            print("** class doesn't exist **")
        else:
            new_obj = eval(command)()
            new_obj.save()
            print(new_obj.id)

    def show(self, line):
        """prints the string representation of an instance
        based on the class name and id"""
        command = self.parseline(line)[0]
        arg = self.parseline(line)[1]
        if command is None:
            print("** class name missing **")
        elif command not in self.our_classes:
            print("** class doesn't exist **")
        elif arg == "":
            print("** instance id missing **")
        else:
            instance = models.storage.all().get(command + "." + arg)
            if instance is None:
                print("** no instance found **")
            else:
                print(instance)

    def destroy(self, line):
        """Deletes an instance based on the class name and id"""
        command = self.parseline(line)[0]
        arg = self.parseline(line)[1]
        if command is None:
            print("** class name missing **")
        elif command not in self.our_classes:
            print("** class doesn't exist **")
        elif arg == "":
            print("** instance id missing **")
        else:
            instance = models.storage.all().get(command + "." + arg)
        if instance is None:
            print("** no instance found **")
        else:
            del models.storage.all()[instance]
            models.storage.save()

    def to_all(self, line):
        """Prints all string representation of all instances
        based or not on the class name"""
        command = self.parseline(line)[0]
        objs = models.storage.all()
        if command is None:
            print([str(obj[obj]) for obj in objs])
        elif command in self.our_classes:
            keys = objs.keys()
            print([str(objs[key]) for key in keys if key.startswith(command)])
        else:
            print("** class doesn't exist **")

    def update(self, line):
        """Updates an instance based on the class name and id
        by adding or updating attribute"""


if __name__ == '__main__':
    HBNBCommand().cmdloop()
