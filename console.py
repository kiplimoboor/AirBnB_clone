#!/usr/bin/python3
"""
This module contains the CLI implementation for the project
"""
import cmd
import json
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
        Deletes an instance based on the class name and id
        """

        args = arg.split() if arg else [False]
        if is_valid_class(args[0], len(args) == 2):
            id = args[1]

            model = find_model(id)
            if model:
                del self.storage[model.__class__.__name__ + '.' + id]
                save_to_file()
            else:
                print("** no instance found **")

    def do_all(self, arg):
        """
        Usage: all BaseModel or all
        Prints all string representation of all instances
        """

        args = arg.split() if arg else [False]
        if args and not is_valid_class(args[0]):
            return

        instances = get_all_instances(args)
        for instance in instances:
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

            if len(args) < 4:
                print("** attribute name missing **")
                return

            if len(args) < 5:
                print("** value missing **")
                return

            model = find_model(id)
            if model:
                setattr(model, attribute_name, attribute_value)
                model.save()
            else:
                print("** no instance found **")


def is_valid_class(arg, id=True):
    """
    Checks if the class is valid.
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
                return saved_models[model]
    return None


def get_all_instances(args):
    """
    Get all instances based on class name or all
    """
    filename = "file.json"
    with open(filename, 'r') as json_file:
        saved_models = json.load(json_file)
        instances = [str(saved_models[model]) for model in saved_models
                     if not args or model.split('.')[0] == args[0]]
        return instances


def save_to_file():
    """
    Save instances to the file
    """
    filename = "file.json"
    with open(filename, 'r') as json_file:
        saved_models = json.load(json_file)
        # Save instances to the file (implement this part according to your data structure)
        # saved_models[new_instance.id] = new_instance
    with open(filename, 'w') as json_file:
        json.dump(saved_models, json_file)


if __name__ == '__main__':
    HBNBCommand().cmdloop()

