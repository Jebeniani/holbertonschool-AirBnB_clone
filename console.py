#!/usr/bin/python3
"""class HBNBCommand"""

import cmd

class HBNBCommand(cmd.Cmd):
    def __init__(self,prompt_name='(hbnb)'):
        super().__init__()
        self.prompt_name = prompt_name

    def do_EOF(self, line):
        return True

    def do_quit(self, line):
        return True


if __name__ == '__main__':
    HBNBCommand().cmdloop()
