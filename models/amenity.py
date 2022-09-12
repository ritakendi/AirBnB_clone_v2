#!/usr/bin/python3
""" An Amenity class that inherits from BaseModel """

from models.base_model import BaseModel


class Amenity(BaseModel):
    """ Inherits from BaseModel,
    instantiate with empty string as values for attributes """
    name = ""
