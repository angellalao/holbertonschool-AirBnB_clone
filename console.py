#!/usr/bin/python3
import cmd
"""Entry point of the command interpreter """


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


if __name__ == '__main__':
    HBNBCommand().cmdloop()
