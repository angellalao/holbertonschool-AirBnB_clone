#!/usr/bin/python3
import cmd, sys

class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb) "

    def emptyline(self):
        """ Override emptyline to do nothing """
        pass

    def do_EOF(self, args):
        """Exits the program"""
        raise SystemExit

    def do_quit(self, args):
        """Quit command to exit the program"""
        return True



if __name__ == '__main__':
    HBNBCommand().cmdloop()
