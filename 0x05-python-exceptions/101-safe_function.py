#!/usr/bin/python3
import sys


def safe_function(fct, *args):
    """
    Executes a function safely, catching exceptions and returning None if an error occurs.

    Parameters:
    fct (callable): The function to execute.
    *args: Arguments to pass to the function.

    Returns:
    The result of the function or None if an exception occurred.
    """
    try:
        return fct(*args)
    except Exception as e:  # Catching all exceptions
        print("Exception: {}".format(e), file=sys.stderr)
        return None
