#!/usr/bin/python3
import sys

def safe_function(fct, *args):
    try:
        res = fct(*args)
    except Exception as e:  # Catching Exception instead of BaseException
        res = None
        print("Exception: {}".format(e), file=sys.stderr)
    return res  # No need for finally here
