#!/usr/bin/python3
"""
Module for State class.
"""

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()


class State(Base):
    """Class representing a state.

    Attributes:
        id (int): The unique identifier for the state.
        name (str): The name of the state.
        cities (relationship): Relationship to the City class.
    """
    __tablename__ = 'states'

    id = Column(Integer, autoincrement=True, primary_key=True)
    name = Column(String(128), nullable=False)
    cities = relationship("City", cascade="all, delete", backref="state")
