#!/usr/bin/python3
"""
the console module
"""
import cmd
import json
from models import storage
from models.base_model import BaseModel


class HBNBCommand(cmd.Cmd):
    """console command processor"""

    prompt = '(hbnb) '

    def do_EOF(self, line):
        """end of file marker the clean close the program"""
        return True

    def do_quit(self, line):
        """quit function to quit the console"""
        return True

    def emptyline(self):
        print('', end='')

    def do_create(self, line):
        """create a new instance of BaseModel"""
        if not line:
            print("** class name missing **")
        elif line != 'BaseModel':
            print("** class doesn't exist **")
        else:
            obj = BaseModel()
            storage.new(obj.to_dict())
            storage.save()
            print(obj.id)

    def do_update(self, line):
        """destroy an existing instance of BaseModel"""
        command = line.strip().split()
        if not command:
            print("** class name missing **")
        elif command[0] != 'BaseModel':
            print("** class doesn't exist **")
        elif len(command) < 2:
            print("** instance id missing **")
        else:
            obj_id = command[0] + '.' + command[1]
            if obj_id not in storage.all():
                print("** no instance found **")
            elif len(command) < 3:
                print("** attribute name missing **")
            elif len(command) < 4:
                print("** value missing **")
            else:
                key = command[2].strip(' \'\"')
                value = command[3].strip(' \'\"')
                storage.update(obj_id, key, value)

    def do_destroy(self, line):
        """destroy an existing instance of BaseModel"""
        command = line.strip().split()
        if not command:
            print("** class name missing **")
        elif command[0] != 'BaseModel':
            print("** class doesn't exist **")
        elif len(command) < 2:
            print("** instance id missing **")
        else:
            try:
                obj_id = command[0] + '.' + command[1]
                storage.delete(obj_id)
            except Exception:
                print("** no instance found **")

    def do_show(self, line):
        command = line.strip().split()
        if not command:
            print("** class name missing **")
        elif command[0] != 'BaseModel':
            print("** class doesn't exist **")
        elif len(command) < 2:
            print("** instance id missing **")
        else:
            try:
                objects = storage.all()
                obj_id = command[0] + '.' + command[1]
                print(objects[obj_id])
            except Exception:
                print("** no instance found **")

    def do_all(self, line):
        command = line.strip().split()
        if not command or command[0] == 'BaseModel':
            objects = []
            for key, value in storage.all().items():
                class_name, obj_id = key.split('.')
                objects.append(f"[{class_name}] ({obj_id}) {value}")
            print(objects)
        else:
            print("** class doesn't exist **")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
