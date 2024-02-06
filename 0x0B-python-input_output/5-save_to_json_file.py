#!/usr/bin/python3
"""
Module for saving an object to a JSON file.
"""
import json


def save_to_json_file(my_obj, filename):
    """
    Writes an object to a text file in JSON format.

    Args:
        my_obj (object): The object to be saved.
        filename (str): The name of the file to save the object to.
    """
    with open(filename, 'w') as file:
        json.dump(my_obj, file)
