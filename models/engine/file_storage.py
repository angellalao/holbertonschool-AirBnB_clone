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
        self.__objects[key] = obj

    def save(self):
        """serializes __objects to the JSON file (path: __file_path)"""
        json_dict = {}
        for key in self.__objects:
            json_dict[key] = self.__objects[key].to_dict()
        with open(self.__file_path, "w") as f:
            json.dump(json_dict, f)

    def reload(self):
        """deserializes the JSON file to __objects"""
        from models.base_model import BaseModel
        reloaded_dict = {}
        try:
            with open(self.__file_path, "r") as f:
                reloaded_dict = json.load(f)
        except:
            reloaded_dict = {}
            pass
        class_dict = {
            "BaseModel": BaseModel
        }
        for key, obj in reloaded_dict.items():
            if obj.get("__class__") in class_dict.keys():
                self.__objects[key] = class_dict[obj["__class__"]](**obj)
