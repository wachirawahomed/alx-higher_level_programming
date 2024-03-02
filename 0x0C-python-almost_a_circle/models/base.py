#!/usr/bin/python3
"""Base module.

Contains the Base class which will be the
“base” of all other classes in this project.
"""

from os import path


class Base:
    """Base class for managing id attribute."""

    __nb_objects = 0

    def __init__(self, id=None):
        """Initializes Base instance

        Args:
            id (init): the identifier of the Base object.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
