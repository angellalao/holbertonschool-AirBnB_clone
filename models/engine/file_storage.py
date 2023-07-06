#!/usr/bin/python3
"""define FileStorage class"""
import json


class FileStorage:
    """class FileStorage"""
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """returns the dictionary __objects"""
        return self.__objects

    def new(self, obj):
        """sets in __objects the obj with key <obj class name>.id"""
        """key should be combination of obj class name and its id"""
        name = type(obj).__name__
        obj_id = str(obj.id)
        key = name + "." + obj_id
        self.__objects[key] = obj.to_dict()


    def save(self):
        """serializes __objects to the JSON file (path: __file_path)"""
        json_obj = json.dumps(self.__objects)
        with open(self.__file_path, "w") as f:
            f.write(json_obj)

    def reload(self):
        """deserializes the JSON file to __objects"""
        try:
            with open(self.__file_path, "r") as f:
                self.__objects = json.load(f)
        except:
            pass
