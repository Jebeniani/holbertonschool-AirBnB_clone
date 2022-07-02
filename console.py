#!/usr/bin/python3
"""class HBNBCommand"""

import cmd


class HBNBCommand(cmd.Cmd):
    """cmd processor class"""
    prompt = '(hbnb)'

    def do_EOF(self, line):
        """EOF command to exit the program"""
        return True

    def do_quit(self, line):
        """Quit command to exit the program"""
        return True

    def emptyline(self):
        """emptyLine\n"""
    pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
