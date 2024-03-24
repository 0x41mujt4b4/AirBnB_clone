#!/usr/bin/python3
"""
the console module
"""
import cmd


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


if __name__ == '__main__':
    HBNBCommand().cmdloop()
