#!/usr/bin/python3
"""
Script to add all arguments to a Python list and save them to a JSON file.
"""

import sys

from 5-save_to_json_file import save_to_json_file
from 6-load_from_json_file import load_from_json_file

# Name of the JSON file
filename = "add_item.json"

# Initialize an empty list
my_list = []

# Check if the JSON file exists
if exists(filename):
    # Load the existing list from the JSON file
    my_list = load_from_json_file(filename)

# Append command-line arguments to the list
my_list.extend(sys.argv[1:])

# Save the updated list to the JSON file
save_to_json_file(my_list, filename)
