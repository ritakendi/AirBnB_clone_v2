#!/usr/bin/python3
""" added comment """
import json
from os import environ
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from models.base_model import BaseModel, Base
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class DBStorage:
    """ SQL database class
    """
    __engine = None
    __session = None
    __clsdict = {"User": User,
                 "State": State,
                 "City": City,
                 "Amenity": Amenity,
                 "Place": Place,
                 "Review": Review
                 }

    def __init__(self):
        """ the initializersz
        """
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.format(
            environ['HBNB_MYSQL_USER'],
            environ['HBNB_MYSQL_PWD'],
            environ['HBNB_MYSQL_HOST'],
            environ['HBNB_MYSQL_DB']),
                               pool_pre_ping=True)

        if 'HBNB_ENV' in environ.keys():
            if environ['HBNB_ENV'] == 'test':
                Base.metadata.drop_all(bind=self.__engine)

    def all(self, cls=None):
        """ returns a dictionary of all objects """
        my_dict = {}
        if cls is None:
            for key, cls in self.__clsdict.items():
                for obj in self.__session.query(cls):
                    my_dict["{}.{}".format(cls.__name__, obj.id)] = obj
        else:
            for obj in self.__session.query(self.__clsdict.get(cls)):
                my_dict["{}.{}".format(
                            self.__clsdict.get(cls).__name__, obj.id)] = obj
        return my_dict

    """
    def all(self, cls=None):
         returns a dictionary of all objects "
        my_dict = {}
        if isinstance(cls, str):
            self.__clsdict.get(cls)
        else:
            cls = cls
        if cls:
            for obj in self.__session.query(cls):
                my_dict["{}.{}".format(cls.__name__, obj.id)] = obj
            return my_dict
        for key, cls in self.__clsdict.items():
            for obj in self.__session.query(cls):
                my_dict["{}.{}".format(cls.__name__, obj.id)] = obj
        return my_dict
    """

    def new(self, obj):
        """ adds object to the current database session """
        self.__session.add(obj)

    def save(self):
        """ commit all changes of the current database session """
        self.__session.commit()

    def delete(self, obj=None):
        """ Deletes from the current database session obj if not None"""
        if obj is not None:
            self.__session.query(obj).delete(synchronize_session=False)

    def reload(self):
        """ create all tables in the database """
        Base.metadata.create_all(self.__engine)
        self.__session = scoped_session(sessionmaker(
            bind=self.__engine,
            expire_on_commit=False))
        """
        factory = sessionmaker(bind=self.__engine, expire_on_commit=True)
        self.__session = scoped_session(factory)()
        """

    def close(self):
        """ closes or removes a private session """
        self.__session.close()
