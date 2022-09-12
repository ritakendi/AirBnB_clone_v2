#!/usr/bin/python3
""" the file storage class """
import json
import os
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class FileStorage:
    """ serializes and deserializes files to JSOn and back """

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """ returns the dictionary __objects """
        return self.__objects

    def new(self, obj):
        """ sets in __objects to the obj with key <obj class name>.id """
        # get the object's class's name, add a . and id
        # so it would be BaseModel.ID
        self.__objects[obj.__class__.__name__ + "." + str(obj.id)] = obj

    def save(self):
        """ serializes __objects to the JSON file path """
        # get all the items in __objects, which are dicts
        # loop through all they keys and values.
        # do dict comprehension, for each key and value(to dictionary method)
        x = json.dumps({k: v.to_dict() for k, v in self.__objects.items()})
        with open(self.__file_path, mode='w', encoding='utf-8') as f:
            f.write(x)

    def reload(self):
        """ deserializes the JSON file to __objects, if path exists or do
        nothing. no exceptions should raise """
        # create a Dict that matched keys with values
        # keys are strings and values are the classes of the values
        obj_dict = {"BaseModel": BaseModel, "User": User, "State": State,
                    "City": City, "Amenity": Amenity, "Place": Place,
                    "Review": Review}
        # check if the file is even there first
        if os.path.isfile(self.__file_path):
            # attempt to open that file and load the string that we read
            with open(self.__file_path, mode='r', encoding='utf-8') as f:
                x = json.loads(f.read())
                for k, v in x.items():
                    self.__objects[k] = obj_dict[v["__class__"]](**v)
                # We read a dict, we iterate or enumerate through it
                # We make a new __object[key] in file storage that
                # Does access magic with the obj_dict. stores in the data
                # It works. You jut need to believe
