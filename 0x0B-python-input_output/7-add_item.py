#!/usr/bin/python3
import sys
from os.path import exists
from 5-save_to_json_file import save_to_json_file
from 6-load_from_json_file import load_from_json_file

# Define the filename
filename = "add_item.json"

# Initialize the list
if exists(filename):
    items = load_from_json_file(filename)
else:
    items = []

# Add command line arguments to the list
items.extend(sys.argv[1:])

# Save the updated list back to the file
save_to_json_file(items, filename)
