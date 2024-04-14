#!/usr/bin/python3
"""
Module for State class.
"""

from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from model_city import Base, City


class State(Base):
    """Class representation of a State for SQLAlchemy.

    Attributes:
    __tablename__ (str): The table name of the class
    id (int): The State id of the class
    name (str): The State name of the class
    cities (:obj:`City`): The Cities belongs to State
    """

    __tablename__ = 'states'
    id = Column(Integer, primary_key=True, nullable=False, unique=True)
    name = Column(String(128), nullable=False)
    cities = relationship("City", backref="state", cascade="all, delete")

