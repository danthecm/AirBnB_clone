#!/usr/bin/python3
"""
A command line module for interacting with
the AirBnB Application
"""
import cmd
from models import base_model, storage, user


class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb) "
    class_list = {"BaseModel": base_model.BaseModel, "User": user.User}

    def emptyline(self):
        pass

    def do_quit(self, args):
        """
        Exists the program by returning True
        if the user types quit and press enter
        """
        return True

    def do_create(self, line):
        """
        Creates a new instance of the given
        class name
        """
        words = line.split(" ")
        if words[0] == "":
            print("** class name missing **")
        elif words[0] not in self.class_list.keys():
            print("** class doesn't exist **")
        else:
            my_class = self.class_list.get(words[0])
            new_model = my_class()
            new_model.save()
            print(new_model.id)

    def do_show(self, line):
        """
        Creates a new instance of the given
        class name
        """
        words = line.split(" ")
        if words[0] == "":
            print("** class name missing **")
        elif words[0] not in self.class_list.keys():
            print("** class doesn't exist **")
        elif len(words) < 2:
            print("** instance id missing **")
        else:
            all_models = storage.all()
            my_model = all_models.get(f"{words[0]}.{words[1]}")
            if my_model:
                print(my_model)
            else:
                print("** no instance found **")

    def do_all(self, line):
        """
        Creates a new instance of the given
        class name
        """
        words = line.split(" ")
        if words[0] == "":
            all_models = storage.all()
            print(all_models)
        elif words[0] not in self.class_list:
            print("** class doesn't exist **")
        else:
            all_models = storage.all()
            all_models = {k: v for k, v in all_models.items(
            ) if v.__class__.__name__ == words[0]}
            print(all_models)

    def do_update(self, line):
        """
        Creates a new instance of the given
        class name
        """
        words = line.split(" ", 3)
        if words[0] == "":
            print("** class name missing **")
        elif words[0] not in self.class_list:
            print("** class doesn't exist **")
        elif len(words) < 2:
            print("** instance id missing **")
        else:
            all_models = storage.all()
            my_model = all_models.get(f"{words[0]}.{words[1]}")
            if my_model:
                if len(words) < 3:
                    print("** attribute name missing **")
                elif len(words) < 4:
                    print("** value missing **")
                elif words[2] in ["id", "created_at", "updated_at"]:
                    print("** can not update attribute **")
                else:
                    setattr(my_model, words[2], words[3])
                    my_model.save()
                    print(my_model.id)
            else:
                print("** no instance found **")

    def do_destroy(self, line):
        """
        Creates a new instance of the given
        class name
        """
        words = line.split(" ")
        if words[0] == "":
            print("** class name missing **")
        elif words[0] not in self.class_list:
            print("** class doesn't exist **")
        elif len(words) < 2:
            print("** instance id missing **")
        else:
            all_models = storage.all()
            my_model = all_models.get(f"{words[0]}.{words[1]}")
            if my_model:
                storage.pop(f"{my_model.__class__.__name__}.{my_model.id}")
                storage.save()
            else:
                print("** no instance found **")

    do_EOF = do_quit


if __name__ == '__main__':
    HBNBCommand().cmdloop()
