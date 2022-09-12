#!/usr/bin/python3
"""Base class Definition"""
import uuid
import models
from datetime import datetime


class BaseModel:
    """ BaseModel definition"""

    def __init__(self, *args, **kwargs):
        """init method to initialize the values
        We ignore all args. No error or handling for that.
        We only care for keyworded arguments"""
        if (kwargs):
            for k, v in kwargs.items():
                if (k == 'created_at' or k == 'updated_at'):
                    setattr(self, k, datetime.strptime(
                          v, "%Y-%m-%dT%H:%M:%S.%f"))
                # if we would a key that matched,
                # set attribute to year, month, day, hour, minutes, sec
                elif k == '__class__':
                    pass
                # we just skip class if that is the key, do not modify that
                else:
                    setattr(self, k, v)
                # set whatever value given to us to the appropriate key
        else:
            # not a dict was given to us. we were given a command like
            # create User. and we will use uuid and date now to instantiate
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

    def __str__(self):
        """ method to format BaseModel for printing.
        We want to override the default __str__ out put to
        name of object and the id and the dict """
        thestr = "[{:s}] ({:s}) {}".format(
              type(self).__name__, self.id, self.__dict__)
        return thestr

    def save(self):
        """ method to save the object.
        We want to update the attribute updated_at with a newer time.
        We then store the model in our storage data base """
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """ make dictionary with instance attributes.
        We store the name of the object as the class.
        We loop through all the attributes and store it in a dict.
        If the attribute was time related, we convert to iso format """
        temp_dict = {}
        temp_dict['__class__'] = type(self).__name__
        for k, v in self.__dict__.items():
            if k == 'created_at' or k == 'updated_at':
                temp_dict[k] = v.isoformat()
            else:
                temp_dict[k] = v
        return temp_dict
