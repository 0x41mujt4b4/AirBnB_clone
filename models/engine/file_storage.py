#!/usr/bin/python3
'''
FileStorage model to store (serialize and deserialize) BaseModel objects
'''
import json


class FileStorage:
    '''
    FileStorage class that serialize and deserialize
    '''
    __file_path = 'file.json'
    __objects = dict()

    def all(self):
        return self.__objects

    def new(self, obj):
        self.__objects[obj['__class__'] + '.' + obj['id']] = obj
    def save(self):
        # serialize objects to the json file (path: __file_path)
        with open(self.__file_path, 'w') as file:
            json.dump(self.__objects, file)

    def reload(self):
        # deserialize the json file to __objects
        # (only if the json file (__file_path) exists;
        # otherwise, do nothing. if the file doesn't exist,
        # no exception should be raised.
        try:
            with open(self.__file_path, 'r') as file:
                self.__objects = json.load(file)
        except Exception as e:
            pass
