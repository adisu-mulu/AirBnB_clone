#!/usr/bin/python3
"""This module defines the command line interpreter"""
import cmd
import sys


class HBNBCommand(cmd.Cmd):
    """Command line interpreter class that inherits Cmd"""
    prompt = "(hbnb) "

    def onecmd(self, line):
        """Overrides parent onecmd method to disable execution
        of previous command in case of blank line + Enter"""
        if line == '':
            return False
        else:
            return super().onecmd(line)

    def cmdloop(self):
        """Overrides the cmdloop method to check for interactive
        vs non-interactive mode"""
        if sys.stdin.isatty():
            return super().cmdloop()
        else:
            HBNBCommand().onecmd(sys.stdin.readline().strip())

    def do_quit(self, arg):
        """Exits the command line interpreter."""
        return True

    def do_EOF(self, arg):
        """Also exits the command line interpreter"""
        return True


if __name__ == '__main__':
    HBNBCommand().cmdloop()
