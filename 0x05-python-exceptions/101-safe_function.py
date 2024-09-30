#!/usr/bin/python3
import sys

def safe_function(fct, *args):
    try:
        # Execute the function with given arguments
        res = fct(*args)
    except BaseException as e:
        # If any exception occurs, set result to None
        res = None
        # Print the exception to stderr
        print("Exception: {}".format(e), file=sys.stderr)
    finally:
        # Always return the result (either the function's result or None)
        return res
