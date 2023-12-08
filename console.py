#!/usr/bin/python3
"""
This module containes the CLI implementation for the project
"""
import cmd
from models.base_model import BaseModel


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
        """
        Skip an empty line
        """
        pass

    def do_create(self, arg):
        """
        Usage: create BaseModel
        Creates a new instance of BaseModel, saves it (to the JSON file)
        and prints the id.
        """

        if not arg:
            print("** class name missing **")
            return
        if arg != 'BaseModel':
            print("** class doesn't exist **")
            return

        new_model = BaseModel()
        new_model.save()
        print(new_model.id)


if __name__ == '__main__':
    HBNBCommand().cmdloop()
