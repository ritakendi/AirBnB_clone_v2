#!/usr/bin/python3
""" A City class that inherits from BaseModel """

from models.base_model import BaseModel


class City(BaseModel):
    """ Inherits from BaseModel,
    instantiate with empty string as values for attributes """
    state_id = ""
    name = ""
