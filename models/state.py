#!/usr/bin/python3
""" A State class that inherits from BaseModel """

from models.base_model import BaseModel


class State(BaseModel):
    """ Inherits from BaseModel,
    instantiate with empty string as values for attributes """
    name = ""
