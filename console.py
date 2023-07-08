#!/usr/bin/python3
"""Entry point of the command interpreter """
import cmd
from models import storage
from models.base_model import BaseModel


class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb) "

    def emptyline(self):
        """ Override emptyline to do nothing\n"""
        pass

    def do_EOF(self, args):
        """Exits the program\n"""
        raise SystemExit

    def do_quit(self, args):
        """Quit command to exit the program\n"""
        return True

    def do_create(self, args):
        """Creates a new instance of BaseModel, saves it to a json\
file and prints the id\n"""
        if len(args) == 0:
            print("** class name missing **")
        elif args != "BaseModel":
            print("** class doesn't exist **")
        else:
            new_instance = BaseModel()
            new_instance.save()
            print(new_instance.id)

    def do_show(self, args):
        """Prints the string representation of an instance based on the class\
 name and id\n """
        args_list = args.split(" ")
        if len(args) == 0:
            print("** class name missing **")
        elif args_list[0] != "BaseModel":
            print("** class doesn't exist **")
        elif (len(args_list) < 2):
            print("** instance id missing **")
        else:
            """not finished yet """
            try:
                print(self)
            except:
                print("** no instance found **")

    def do_destroy():
        pass

    def do_all():
        pass

    def do_update():
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
