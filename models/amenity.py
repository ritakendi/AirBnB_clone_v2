#!/usr/bin/python3
"""
Amenity module for HBNB project
"""
import models
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from models.place import place_amenity


class Amenity(BaseModel, Base):
    """
    This class Represents Amenities for a place

    Inherits the BaseModel and Base(from sqlachemy)and links to the mysql
    table amenities.
    Attributes:
    __tablename__(str): name of the MYSQL table
        name(sqlalchemy string): name of the City
    """
    __tablename__ = "amenities"
    name = Column(String(128), nullable=False)
    place_amenities = relationship('Place', secondary=place_amenity,
                                   backref='amenities')
