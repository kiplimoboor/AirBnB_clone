#!/usr/bin/python3
"""
This module containes the CLI implementation for the project
"""
import cmd
import json
import re
from datetime import datetime
from models import storage
from models.base_model import BaseModel
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User

classes = {'Amenity': Amenity, 'BaseModel': BaseModel, 'City': City,
           'Place': Place, 'Review': Review, 'State': State,
           'User': User}


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
            new_model = classes[arg]()
            storage.save()
            print(new_model.id)
            return

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
                print(to_str(saved_models[model]))

    def do_destroy(self, arg):
        """
        Usage: destroy BaseModel model-id
        Deletes an instance based on the class name an id
        """

        args = arg.split() if arg else [False]
        if is_valid_input(args[0], len(args) == 2):
            id = args[1]

            saved_models = storage.all()
            model = find_model(saved_models, id)
            if model:
                del saved_models[model]
                storage.save()

    def do_all(slef, arg):
        """
        Usage: all BaseModel or all
        Prins all string representation of all instances
        """

        saved_models = storage.all()

        if arg:
            if is_valid_input(arg):
                print(
                    [f"{to_str(saved_models[model])}"
                     for model in saved_models
                     if saved_models[model]['__class__'] == arg])
        else:
            print([f"{to_str(saved_models[model])}" for model in saved_models])

    def do_update(self, arg: str):
        """
        Usage: update BaseModel model-id attribute value
        Updates an instance based on the class name and id
        """

        args = arg.split(maxsplit=3) if arg else [False]
        if is_valid_input(args[0], len(args) > 1,
                          len(args) > 2, len(args) > 3):
            id = args[1]
            attr = args[2]
            value = re.findall(r"^[\"\'](.*?)[\"\']", args[3])[0]

            print(value)
            saved_models = storage.all()

            model = find_model(saved_models, id)

            if model:
                saved_models[model][attr] = value
                storage.save()


def is_valid_input(arg, id=True, attribute=True, value=True):
    """
    Checks if class is valid.
    id is optional
    """
    if not arg:
        print("** class name missing **")
        return False
    if arg not in classes.keys():
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


def find_model(models, id):
    for model in models:
        if model.split('.')[1] == id:
            return model

    print("** no instance found **")
    return False


def to_str(obj):
    return str(classes[obj['__class__']](**obj))


if __name__ == '__main__':
    HBNBCommand().cmdloop()
