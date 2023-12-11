#!/usr/bin/python3
"""
This module containes the CLI implementation for the project.
It contains the entry pooint of the command intepreter.
The module defines a class HBNBCommand that interpretes commands given to it.
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


classes = {'BaseModel': BaseModel, 'User': User, 'City': City,
           'Place': Place, 'Amenity': Amenity, 'Review': Review,
           'State': State}


class HBNBCommand(cmd.Cmd):
    """
    This class defines the HBNB command interpreter.
    Properties:
      prompt: (HBNB)
      it contains different methods used in controlling the
      command interpreter
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
            if arg in classes:
                new_model = classes[arg]()
                storage.save()
                print(new_model.id)
            else:
                print("** class doesn't exist **")
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
                del saved_models[model]
                storage.save()
            else:
                print("** no instance found **")

    def do_all(slef, arg):
        """
        Usage: all BaseModel or all
        Prins all string representation of all instances
        """

        saved_models = storage.all()

        if arg:
            if is_valid_input(arg):
                print(
                    [f"{saved_models[model]}"
                     for model in saved_models
                     if type(saved_models[model]).__name__ == arg])
        else:
            print([f"{saved_models[model]}" for model in saved_models])

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
            value = args[3].strip('\"')

            saved_models = storage.all()

            model = find_model(saved_models, id)

            if model:
                setattr(saved_models[model], attr, value)
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
        print("** instance id missing **")
        return False
    if not attribute:
        print("** attribute name missing **")
        return False
    if not value:
        print("** value missing **")
        return False

    return True


def find_model(models, id):
    """
    Find and return a model instance based on given ID
    """
    for model_key, model_instance in models.items():
        if model_key.split('.')[1] == id:
            return model_instance

    print("** no instance found **")
    return False


if __name__ == '__main__':
    HBNBCommand().cmdloop()
