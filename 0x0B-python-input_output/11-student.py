#!/usr/bin/python3
"""Student module.

Contains a Student class and some methods.
"""

class Student:
    """Defines a student by first_name, last_name, and age."""

    def __init__(self, first_name, last_name, age):
        """
        Initialize a Student instance with first_name, last_name, and age.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Retrieve a dictionary representation of a Student instance.

        If attrs is a list of strings, only attributes with names contained
        in the list are retrieved. Otherwise, all attributes are retrieved.
        """
        if attrs is None:
            return self.__dict__
        else:
            return {attr: getattr(self, attr)
                    for attr in attrs if hasattr(self, attr)}

    def reload_from_json(self, json):
        """
        Replace all attributes of the Student instance with
        the values from the provided dictionary.
        """
        for key, value in json.items():
            setattr(self, key, value)

