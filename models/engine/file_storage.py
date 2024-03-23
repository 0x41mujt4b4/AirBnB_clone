#!/usr/bin/python3
'''
FileStorage model to store (serialize and deserialize) BaseModel objects
'''


class FileStorage:
    '''
    FileStorage class that serialize and deserialize
    '''
    __file_path = ''
    __objects = dict()

    def __init__(self):
        pass

    def all(self):
        return self.__objects

    def new(self, obj):
        self.__objects[self.__class__.__name__.id] = obj

    def save(self):
        # serialize objects to the json file (path: __file_path)
        pass

    def reload(self):
        # deserialize the json file to __objects
        # (only if the json file (__file_path) exists;
        # otherwise, do nothing. if the file doesn't exist,
        # no exception should be raised.
        pass
