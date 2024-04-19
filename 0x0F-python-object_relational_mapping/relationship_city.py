#!/usr/bin/python3
"""Module to define the City class"""
from sqlalchemy import Column, Integer, String, ForeignKey
from relationship_state import Base


class City(Base):
    """Class representing a city

    Attributes:
        __tablename__ (str): The table name of the class
        id (int): id of the city.
        name (str): name of the city.
        state_id (int): id of the associated state.
    """

    __tablename__ = 'cities'
    id = Column(Integer, autoincrement=True, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
