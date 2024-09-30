import sys

def safe_function(fct, *args):
    try:
        # Try to execute the function with its arguments
        return fct(*args)
    except Exception as e:
        # Print the exception message to stderr with "Exception: " prefix
        print("Exception: {}".format(e), file=sys.stderr)
        return None

