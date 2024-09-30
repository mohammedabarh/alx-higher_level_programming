#!/usr/bin/python3

import sys

def safe_function(fct, *args):
    try:
        # Execute the function with the provided arguments
        return fct(*args)
    except Exception as e:
        # Catch any exception and print the error message to stderr
        print(f"Exception: {e}", file=sys.stderr)
        return None

