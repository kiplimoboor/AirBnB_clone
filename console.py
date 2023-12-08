#!/usr/bin/python3
"""
This module containes the CLI implementation for the project
"""
import cmd
import json
import re
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

        if is_valid_class(arg):
            new_model = BaseModel()
            new_model.save()
            print(new_model.id)

    def do_show(self, arg):
        """
        Usage: show BaseModel model-id
        Prints the string representation of an instance based
        on the class name and id
        """

        args = arg.split() if arg else [False]
        if is_valid_class(args[0], len(args) == 2):
            id = args[1]

            model = find_model(id)
            if model:
                print(model)

    def do_destroy(self, arg):
        """
        Usage: destroy BaseModel model-id
        Deletes an instance based on the class name an id
        """

        args = arg.split() if arg else [False]
        if is_valid_class(args[0], len(args) == 2):
            id = args[1]

            model = find_model(id)
            if model:
                del model
                save_to_file()
            else:
                print("** no instance found **")

    def do_all(slef, arg):
        """
        Usage: all BaseModel or all
        Prins all string representation of all instances
        """

        args = arg.split() if arg else [False]
        if args and not is_valid_class(args[0]):
            return

        instances = get_all_instances(args)
        print(instances)

    def do_update(self, arg):
        """
        Usage: update BaseModel model-id attribute value
        Updates an instance based on the class name and id
        """

        args = arg.split() if arg else [False]
        if is_valid_class(args[0], len(args) == 4):
            id = args[1]
            attribute_name = args[2]
            attribute_value = args[3]

            model = find_model(id)
            if model:
                setattr(model, attribute_name, eval(attribute_value))
                model.save()
            else:
                print("** no instance found **")

def is_valid_class(arg, id=True):
    """
    Checks if class is valid. 
    id is optional
    """
    if not arg:
        print("** class name missing **")
        return False
    if arg != 'BaseModel':
        print("** class doesn't exist **")
        return False
    if not id:
        print(" ** instance id missing **")
        return False

    return True


def find_model(id):
    """
    Find stored models based on id
    """
    filename = "file.json"
    with open(filename, 'r') as json_file:
        saved_models = json.load(json_file)
        for model in saved_models:
            if model.split('.')[1] == id:
                return saved_models[str(model)]
            else:
                print("** no instance found **")
                return False


if __name__ == '__main__':
    HBNBCommand().cmdloop()
