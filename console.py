#!/usr/bin/python3
"""This module defines the command line interpreter"""
import cmd
import sys
import shlex
from models.base_model import BaseModel
from models.user import User
from models.engine.file_storage import FileStorage


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
        """Quit command to exit the program."""
        return True

    def do_create(self, arg):
        """This method creates new objects """
        if len(arg) < 1:
            print("** class name missing **")
        else:
            arg = arg.split()
            if arg[0] == 'BaseModel':
                bs = BaseModel()
                bs.save()
                print(bs.id)
            if arg[0] == 'User':
                bs = User()
                bs.save()
                print(bs.id)
            else:
                print("** class doesn't exist **")

    def do_show(self, arg):
        """This method shows an instance given classname and id"""
        if len(arg) < 1:
            print("** class name missing **")
        else:
            args = arg.split()
            if not any(args[0] in mylist for mylist in
                       FileStorage()._FileStorage__objects):
                print("** class doesn't exist **")
            else:
                if len(args) < 2:
                    print(" ** instance id is missing **")
                else:
                    obj_name = args[0] + '.' + args[1]
                    if obj_name in FileStorage()._FileStorage__objects:
                        print(FileStorage._FileStorage__objects[obj_name])
                    else:
                        print("** no instance found **")

    def do_destroy(self, arg):
        """Destroys an instance given classname and id"""
        if len(arg) < 1:
            print("** class name missing **")
        else:
            args = arg.split()
            if not any(args[0] == mylist.__class__.__name__ for key, mylist in
                       FileStorage()._FileStorage__objects.items()):
                print("** class doesn't exist **")
            else:
                if len(args) < 2:
                    print(" ** instance id is missing **")
                else:
                    obj_name = args[0] + '.' + args[1]
                    if obj_name in FileStorage()._FileStorage__objects:
                        del FileStorage()._FileStorage__objects[obj_name]
                        FileStorage().save()
                    else:
                        print("** no instance found **")

    def do_all(self, arg):
        """List all available instances"""
        if len(arg) == 0:
            if FileStorage()._FileStorage__objects:
                obj_list = []
                for objs in FileStorage()._FileStorage__objects.values():
                    obj_list.append(str(objs))
                print(obj_list)
            else:
                print("** class doesn't exist **")
        else:
            args = arg.split()
            if not any(args[0] == mylist.__class__.__name__ for key, mylist in
                       FileStorage()._FileStorage__objects.items()):
                print("** class doesn't exist **")
            else:
                objlist = []
                for key, mylist in FileStorage()._FileStorage__objects.items():
                    if mylist.__class__.__name__ == args[0]:
                        objlist.append(str(mylist))
                print(objlist)

    def do_update(self, arg):
        """Updates an instance with new attribute"""
        if len(arg) < 1:
            print("** class name missing **")
        else:
            args = shlex.split(arg)
            if not any(args[0] == mylist.__class__.__name__ for key, mylist in
                       FileStorage()._FileStorage__objects.items()):
                print("** class doesn't exist **")
            else:
                if len(args) < 2:
                    print(" ** instance id is missing **")
                else:
                    obj_name = args[0] + '.' + args[1]
                    if obj_name in FileStorage()._FileStorage__objects:
                        if len(args) < 3:
                            print("** attribute name missing **")
                        elif len(args) < 4:
                            print("** value missing **")
                        else:
                            temp = FileStorage()._FileStorage__objects
                            for k, v in temp.items():
                                if v.id == args[1]:
                                    setattr(v, args[2], args[3])
                                    FileStorage().save()
                    else:
                        print("** no instance found **")

    def do_EOF(self, arg):
        """Quit the program"""
        return True


if __name__ == '__main__':
    HBNBCommand().cmdloop()
