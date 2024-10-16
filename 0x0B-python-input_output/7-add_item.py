#!/usr/bin/python3
"""7-add_item.py
Adds all command line arguments to a list and saves them to a JSON file.
"""

import sys
from load_from_json_file import load_from_json_file
from save_to_json_file import save_to_json_file

filename = 'add_item.json'

# Load existing items from the file, or initialize an empty list if the file doesn't exist.
try:
    items = load_from_json_file(filename)
except FileNotFoundError:
    items = []

# Add command line arguments (excluding the script name) to the list.
items.extend(sys.argv[1:])

# Save the updated list back to the JSON file.
save_to_json_file(items, filename)
