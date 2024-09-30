#!/usr/bin/python3
import sys

def safe_function(fct, *args):
    try:
        return fct(*args)
    except Exception as e:  # Catching general exceptions
        print("Exception: {}".format(e), file=sys.stderr)
        return None  # Return None if an exception occurs
