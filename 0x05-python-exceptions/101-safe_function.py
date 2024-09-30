#!/usr/bin/python3
import sys

def safe_print_integer_err(value):
    try:
        print("{:d}".format(value))  # Attempt to format and print the value as an integer
        return True
    except (ValueError, TypeError) as e:
        print("Exception: {}".format(e), file=sys.stderr)  # Print the error message to stderr
        return False
