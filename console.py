#!/usr/bin/python3
"""
A command line module for interacting with
the AirBnB Application
"""
import cmd


class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb) "

    def do_EOF(self, args):
        """
        Exists the program by returning True
        if the user uses Ctrl+Z
        """
        return True

    def do_quit(self, args):
        """
        Exists the program by returning True
        if the user types quit and press enter
        """
        return True


if __name__ == '__main__':
    HBNBCommand().cmdloop()
