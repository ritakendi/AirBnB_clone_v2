#!/usr/bin/python3
'''
    Define class FileStorage
'''
import json
import models
from models.amenity import Amenity
from models.base_model import BaseModel
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User


class FileStorage:
    '''
        Serializes instances to JSON file and deserializes to JSON file.
    '''
    __file_path = "file.json"
    __objects = {}

    def all(self, cls=None):
        '''
            Return the dictionary
        '''
        if cls:
            if type(cls) == str:
                return {k: v for k, v in self.__objects.items()
                        if type(v) == eval(cls)}
            else:
                return {k: v for k, v in self.__objects.items()
                        if type(v) == cls}
        return self.__objects

    def delete(self, obj=None):
        """ delete an object from the dictionary

        Args:
            obj (object) object in the dictionary
        """
        if obj:
            try:
                del FileStorage.__objects[str(obj.__class__.__name__)
                                          + "."
                                          + str(obj.id)]
            except KeyError:
                pass

    def new(self, obj):
        '''
            Set in __objects the obj with key <obj class name>.id
            Aguments:
                obj : An instance object.
        '''
        key = str(obj.__class__.__name__) + "." + str(obj.id)
        value_dict = obj
        FileStorage.__objects[key] = value_dict

    def save(self):
        '''
            Serializes __objects attribute to JSON file.
        '''
        objects_dict = {}
        for key, val in FileStorage.__objects.items():
            objects_dict[key] = val.to_dict()

        with open(FileStorage.__file_path, mode='w', encoding="UTF8") as fd:
            json.dump(objects_dict, fd)

    def reload(self):
        '''
            Deserializes the JSON file to __objects.
        '''
        try:
            with open(FileStorage.__file_path, encoding="UTF8") as fd:
                FileStorage.__objects = json.load(fd)
            for key, val in FileStorage.__objects.items():
                class_name = val["__class__"]
                class_name = models.classes[class_name]
                FileStorage.__objects[key] = class_name(**val)
        except FileNotFoundError:
            pass

    def close(self):
        '''
            call reload() method for deserializing the JSON file to objects
        '''
        self.reload()
