#!/usr/bin/python3
""" An User class that inherits from BaseModel """

from models.base_model import BaseModel


class User(BaseModel):
    """ Inherits from BaseModel,
    instantiate with empty string as values for attributes """
    email = ""
    password = ""
    first_name = ""
    last_name = ""
