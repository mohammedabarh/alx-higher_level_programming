#!/usr/bin/python3
import sys

def safe_function(fct, *args):
    try:
        # Execute the function with given arguments
        num = fct(*args)
        return num
    except Exception as err:
        # If an exception occurs, print it to stderr and return None
        print("Exception: {}".format(err), file=sys.stderr)
        return None
