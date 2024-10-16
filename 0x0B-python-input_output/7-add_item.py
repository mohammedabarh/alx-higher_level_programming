#!/usr/bin/python3
"""Script that adds all arguments to a Python list and saves them to a file."""
import sys
from os import path
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

# Name of the file to save the list
filename = "add_item.json"

# Initialize an empty list
my_list = []

# If the file exists, load its contents
if path.exists(filename):
    my_list = load_from_json_file(filename)

# Add command line arguments to the list
my_list.extend(sys.argv[1:])

# Save the updated list to the file
save_to_json_file(my_list, filename)
