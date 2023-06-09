#!/usr/bin/python3
"""
A command line module for interacting with
the AirBnB Application
"""
import cmd
from models import (base_model, storage, user, state,
                    city, place, amenity, review)
import re


class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb) "
    class_list = {
        "BaseModel": base_model.BaseModel, "User": user.User,
        "State": state.State, "City": city.City, "Place": place.Place,
        "Amenity": amenity.Amenity, "Review": review.Review}

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
            all_models = {k: str(v) for k, v in all_models.items(
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

    def do_count(self, line):
        """
        Creates a new instance of the given
        class name
        """
        words = line.split(" ", 2)
        if words[0] == "":
            print("** class name missing **")
        elif words[0] not in self.class_list:
            print("** class doesn't exist **")
        else:
            all_models = storage.all()
            my_model = [model for model in all_models.values(
            ) if model.__class__.__name__ == words[0]]
            print(len(my_model))

    def default(self, line: str) -> None:
        action_list = {
            "show": self.do_show, "all": self.do_all, "count": self.do_count,
            "update": self.do_update, "destroy": self.do_destroy}
        words = line.split(".")
        try:
            model = words[0]
            action = words[1]
            class_name = self.class_list.get(model)
            if not class_name:
                return super().default(line)
            start_param = action.index("(")
            end_param = action.index(")")
            actual_word = action[:start_param]
            if actual_word not in action_list:
                return super().default(line)
            params = action[start_param + 1: end_param]
            do_action = action_list.get(actual_word)
            space_rep = [",", "'", '"']
            clean_param = params
            for i in range(len(space_rep)):
                clean_param = clean_param.replace(space_rep[i], "")
            do_action(model + " " + clean_param)
        except Exception as e:
            return super().default(line)

    do_EOF = do_quit


if __name__ == '__main__':
    HBNBCommand().cmdloop()
