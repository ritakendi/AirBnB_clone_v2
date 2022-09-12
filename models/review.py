#!/usr/bin/python3
""" A Review class that inherits from BaseModel """

from models.base_model import BaseModel


class Review(BaseModel):
    """ Inherits from BaseModel,
    instantiate with empty string as values for attributes """
    place_id = ""
    user_id = ""
    text = ""
