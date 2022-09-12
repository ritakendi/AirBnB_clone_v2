#!/usr/bin/python3
""" 
    Implementation of the user class which inherits from BaseModel 
"""

import imp
from models.base_model import BaseModel
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship


class User(BaseModel):
    """ 
        Defination of the User class
    """
    email = Column(String(128), nullable=False)
    password = Column(String(128), nullable=False)
    first_name = Column(String(128), nullable=True)
    last_name = Column(String(128), nullable=True)
    places = relationship("Place", backref="user",
                          cascade="all, delete-orphan")
    reviews = relationship("Review", backref="user",
                           cascade="all, delete-orphan")
