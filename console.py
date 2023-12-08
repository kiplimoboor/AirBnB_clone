#!/usr/bin/python3
"""
This module containes the CLI implementation for the project
"""
import cmd


class HBNBCommand(cmd.Cmd):
    """
    Class to run the cmd implementation
    """

    prompt = "(hbnb) "

    def do_quit(self, arg):
        """Quit command to exit the program\n"""
        return True

    def do_EOF(self, arg):
        """Quit command to exit the program\n"""
        print()
        return True

    def emptyline(self):
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
