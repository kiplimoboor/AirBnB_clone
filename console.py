#!/usr/bin/python3
"""
This module contains the CLI implementation for the project
"""
import cmd
import json
from models.base_model import BaseModel
from models import storage


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

        if is_valid_input(arg):
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
        if is_valid_input(args[0], len(args) == 2):
            id = args[1]

            saved_models = storage.all()
            model = find_model(saved_models, id)
            if model:
                print(saved_models[model])

    def do_destroy(self, arg):
        """
        Usage: destroy BaseModel model-id
        Deletes an instance based on the class name and id
        """

        args = arg.split() if arg else [False]
        if is_valid_input(args[0], len(args) == 2):
            id = args[1]

            saved_models = storage.all()
            model = find_model(saved_models, id)
            if model:
<<<<<<< HEAD
                del self.storage[model.__class__.__name__ + '.' + id]
                save_to_file()
            else:
                print("** no instance found **")
=======
                del saved_models[model]
                storage.save()
                return
>>>>>>> refs/remotes/origin/main

    def do_all(self, arg):
        """
        Usage: all BaseModel or all
        Prints all string representation of all instances
        """

        saved_models = storage.all()

<<<<<<< HEAD
        instances = get_all_instances(args)
        for instance in instances:
            print(instances)
=======
        if arg:
            if is_valid_input(arg):
                print(
                    [f"{str(saved_models[model])}"
                     for model in saved_models
                     if saved_models[model]['__class__'] == arg])
        else:
            print([f"{str(saved_models[model])}" for model in saved_models])
>>>>>>> refs/remotes/origin/main

    def do_update(self, arg):
        """
        Usage: update BaseModel model-id attribute value
        Updates an instance based on the class name and id
        """

        args = arg.split() if arg else [False]
        if is_valid_input(args[0], len(args) > 1, len(args) > 2, len(args) > 3):
            id = args[1]
            attr = args[2]
            value = args[3]

            saved_models = storage.all()

            model = find_model(saved_models, id)

<<<<<<< HEAD
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
=======
            if model:
                saved_models[model][attr] = value
                storage.save()


def is_valid_input(arg, id=True, attribute=True, value=True):
>>>>>>> refs/remotes/origin/main
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
    if not attribute:
        print("** attribute name missing **")
        return False
    if not value:
        print("value missing")
        return False

    return True


<<<<<<< HEAD
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
=======
def find_model(models, id):
    for model in models:
        if model.split('.')[1] == id:
            return model

    print("** no instance found **")
    return False
>>>>>>> refs/remotes/origin/main


if __name__ == '__main__':
    HBNBCommand().cmdloop()

