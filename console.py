#!/usr/bin/python3
"""class HBNBCommand"""

import cmd

class HBNBCommand(cmd.Cmd):
    """CLI"""
    prompt = '(hbnb)'

    def do_EOF(self, line):
        return True

    def do_quit(self, line):
        return True


if __name__ == '__main__':
    HBNBCommand().cmdloop()
