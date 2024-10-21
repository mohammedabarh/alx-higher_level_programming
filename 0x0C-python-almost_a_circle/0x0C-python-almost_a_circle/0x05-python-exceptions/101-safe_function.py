#!/usr/bin/python3
import sys


def safe_function(fct, *args):
    try:
        tr = fct(*args)
    except BaseException as e:
        tr = None
        print("Exception: {}".format(e), file=sys.stderr)
    finally:
        return tr
